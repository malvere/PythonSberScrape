#%%
import asyncio
from time import sleep

from playwright.async_api import Browser, Locator, async_playwright

from config import db_params
from db import ProductDatabase

url = 'https://megamarket.ru/catalog/smartfony/'
url = 'https://megamarket.ru/catalog/?q=моторное%20масло%205л'
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"}

class Prigozhin():
    def __init__(self):
        self.product_db = ProductDatabase(db_params)
    async def go(self):
        await self.start()
        await self.create_context_page()
        # await self.go_sber()
        
    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser: Browser = await self.playwright.webkit.launch(headless=True)
        self.product_db.connect()
        self.product_db.create_table()
        return self
    
    async def create_context_page(self, proxy = None):
        context = await self.browser.new_context()
        self.page = await context.new_page()
        return self
    
    async def go_sber(self):
        page = self.page
        page.on("request", lambda request: print( 
	        ">>", request.method, request.url,
            request.resource_type)) 
        page.on("response", lambda response: print( 
	        "<<", response.status, response.url))
        await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        await page.goto(url)
        try:
            await page.wait_for_load_state("networkidle", timeout=30000)
        except:
            await page.reload(timeout=30000, wait_until="networkidle")
        print(await page.title())
        mobs = await page.locator('.item-block').all()
        print(f"Found {len(mobs)} items.")
        return mobs
    
    async def graceful_shutdown(self):
        self.product_db.close()
        await self.browser.close()
        await self.playwright.stop()
        

    async def parse(self, mobs):
        async def get_text_content(mob: Locator, selector: str):
            try:
                return await mob.locator(selector).text_content(timeout=500)
            except:
                return "0"
        async def get_item_atr(mob: Locator, atr: str):
            try:
                return await mob.locator(".ddl_product_link").get_attribute(atr)
            except:
                return "None"
        for mob in mobs:
            tasks = [
                get_text_content(mob, ".item-title"),
                get_text_content(mob, ".item-price"),
                get_text_content(mob, ".bonus-amount"),
                get_text_content(mob, ".bonus-percent"),
                get_text_content(mob, ".discount-percentage__value"),
                get_item_atr(mob, "data-product-id"),
                get_item_atr(mob, "href"),
            ]
            results = await asyncio.gather(*tasks)
            title, price, bonus, bonusPercent, discount, prodID, link = map(str.strip, results)
            data = {
                "title": title,
                "price": int("".join(filter(str.isdigit, price))),  # Ensure price is an integer or 0
                "bonuses": int("".join(filter(str.isdigit, bonus))),  # Ensure bonuses is an integer or 0
                "bonus_percent": int("".join(filter(str.isdigit, bonusPercent))),  # Ensure bonus_percent is a float or 0.0
                "discount": int("".join(filter(str.isdigit, discount))),  # Ensure discount is an integer or 0
                "product_id": int(prodID) if prodID.isdigit() else 0,  # Ensure product_id is an integer or 0
                "link": link,
            }
            print(
                f"Title: {title}",
                f"Price: {price}",
                f"Bonuses: {bonus}",
                f"Bonus Percent: {bonusPercent}",
                f"Discount: {discount}",
                f"Product ID: {prodID}",
                f"Link: https://megamarket.ru{link}",
                sep='\n')
            print('-' * 20)
            self.product_db.add_product(data)
        self.product_db.commit()
        self.product_db.close()



# %%
async def main():
    bot = Prigozhin()
    await bot.go()
    mobs = await bot.go_sber()
    await bot.parse(mobs)
    await asyncio.sleep(1)
    await bot.graceful_shutdown()
    return bot
asyncio.run(main())
# %%
