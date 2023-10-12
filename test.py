# for mob in mobs:
#     title = mob.locator('.item-title')
#     price = mob.locator('.item-price')
#     bonus = mob.locator('.bonus-amount')
#     bonusPercent = mob.locator('.bonus-percent')
#     print(f'{title.text_content()}\n{price.text_content()}\n{bonus.text_content()}\n{bonusPercent.text_content()}')
# d
#     for mob in mobs:
#             title: str = await mob.locator('.item-title').text_content()
#             price: str = await mob.locator('.item-price').text_content()
#             bonus: str = await mob.locator('.bonus-amount').text_content()
#             bonusPercent: str = await mob.locator('.bonus-percent').text_content()
#             print(
#                 f"Title: {title.strip()}",
#                 f"Price: {price.strip()}",
#                 f"Bonuses: {bonus.strip()}",
#                 f"Bonus Percent: {bonusPercent.strip()}",
#                 sep='\n')
#             print(f"{'-'*20}")

t = [
    "hi",
    "im",
    "Ben"]
a, b, c = map(str.strip, t)
print()
from config import db_params
from db import ProductDatabase

d = {
    "title": "Масло моторное  синтетическое",
    "price": 2590,
    "bonuses": 26,
    "bonus_percent": 1.0,
    "discount": 0,
    "product_id": 600011571747,
    "link": "/catalog/details/maslo-motornoe-sintec-platinum-7000-sae-0w-20-ilsac-gf-6a-5l-41-sinteticheskoe-600011571747/#?related_search=моторное масло 5л"
}

data = map(str.strip, d)
print(data)
# Create an instance of the ProductDatabase class
product_db = ProductDatabase(db_params)
# Connect to the database
product_db.connect()
# Create the table if it doesn't exist
product_db.create_table()
# Add product data
product_db.add_product(d)
# Commit changes
product_db.commit()
# Close the database connection
product_db.close()