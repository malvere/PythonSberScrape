
from time import sleep

from playwright.sync_api import Page, expect, sync_playwright

url = 'https://megamarket.ru/catalog/smartfony-android/'
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"}

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    print(page.title())
    mobs = page.query_selector_all('.item-block')
    sleep(3)
   




# %%
