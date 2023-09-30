#%%
import asyncio
from time import sleep

from playwright.async_api import Browser, Locator, Page, async_playwright, expect

url = 'https://megamarket.ru/catalog/smartfony/'
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"}

class Prigozhin():
    async def go(self):
        await self.start()
        await self.create_context_page()
        # await self.go_sber()
        
    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser: Browser = await self.playwright.webkit.launch(headless=False)
        return self
    
    async def create_context_page(self, proxy = None):
        context = await self.browser.new_context()
        self.page = await context.new_page()
        return self
    
    async def go_sber(self):
        page = self.page
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        print(await page.title())
        mobs = await page.locator('.item-block').all()
        print(f"Found {len(mobs)} items.")
        return mobs
    
    async def graceful_shutdown(self):
        await self.browser.close()
        await self.playwright.stop()

    async def parse(self, mobs):
        
        async def get_text_content(mob: Locator, selector: str):
            try:
                return await mob.locator(selector).text_content(timeout=500)
            except:
                return "0"
        for mob in mobs:
            tasks = [
                get_text_content(mob, ".item-title"),
                get_text_content(mob, ".item-price"),
                get_text_content(mob, ".bonus-amount"),
                get_text_content(mob, ".bonus-percent"),
            ]
            results = await asyncio.gather(*tasks)
            title, price, bonus, bonusPercent = map(str.strip, results)
            print(
                f"Title: {title}",
                f"Price: {price}",
                f"Bonuses: {bonus}",
                f"Bonus Percent: {bonusPercent}",
                sep='\n')
            print('-' * 20)


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
