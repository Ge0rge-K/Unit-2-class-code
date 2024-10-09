cat_age = int(input("Enter the age of the Cat you would like to buy: "))

if cat_age <= 6:
    print(f"The price of the kitten is $250")
elif cat_age <= 11:
    print(f"The price of the teenager is $225")
elif cat_age <= 95:
    print(f"The price of the adult is $125")
elif cat_age >= 96:
    print(f"The price of the senior is $50")