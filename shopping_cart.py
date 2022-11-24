foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of the item you are buying (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: €"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(f"{food}")

for price in prices:
    total += price
print()
print(f"Your total is: €{total}")
