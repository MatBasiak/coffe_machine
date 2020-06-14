# stage 1
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# stage 2

# # Write your code here
# print("Write how many cups of coffee you will need:")
# number_of_coffees = int(input("> "))
# print("For", number_of_coffees, " cups of coffee you will need:")
# water = 200
# milk = 50
# coffee = 15
# print(number_of_coffees * water, "ml of water")
# print(number_of_coffees * milk, "ml of milk")
# print(number_of_coffees * coffee, "g of coffee beans")

# stage 3
print("Write how many ml of water the coffee machine has:")
water_supply = int(input("> "))
print("Write how many ml of milk the coffee machine has:")
milk_supply = int(input("> "))
print("Write how many grams of coffee beans the coffee machine has:")
coffee_supply = int(input("> "))
print("Write how many cups of coffee you will need:")
number_of_coffees = int(input("> "))

water = 200
milk = 50
coffee = 15
# how many coffes can make with supply provided
n_by_water = water_supply // water
n_by_milk = milk_supply // milk
n_by_coffee = coffee_supply // coffee
# minimum value is amount of coffes coffee machine can make
n_total = min(n_by_milk, n_by_water, n_by_coffee)

if number_of_coffees == n_total:
    print("Yes, I can make that amount of coffee")
elif number_of_coffees > n_total:
    print("No, I can make only", n_total, "cups of coffee")
elif number_of_coffees < n_total:
    print("Yes, I can make that amount of coffee (and even",
          n_total - number_of_coffees, "more than that)")
