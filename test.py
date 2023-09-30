for mob in mobs:
    title = mob.locator('.item-title')
    price = mob.locator('.item-price')
    bonus = mob.locator('.bonus-amount')
    bonusPercent = mob.locator('.bonus-percent')
    print(f'{title.text_content()}\n{price.text_content()}\n{bonus.text_content()}\n{bonusPercent.text_content()}')

    for mob in mobs:
            title: str = await mob.locator('.item-title').text_content()
            price: str = await mob.locator('.item-price').text_content()
            bonus: str = await mob.locator('.bonus-amount').text_content()
            bonusPercent: str = await mob.locator('.bonus-percent').text_content()
            print(
                f"Title: {title.strip()}",
                f"Price: {price.strip()}",
                f"Bonuses: {bonus.strip()}",
                f"Bonus Percent: {bonusPercent.strip()}",
                sep='\n')
            print(f"{'-'*20}")