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
# print("Write how many ml of water the coffee machine has:")
# water_supply = int(input("> "))
# print("Write how many ml of milk the coffee machine has:")
# milk_supply = int(input("> "))
# print("Write how many grams of coffee beans the coffee machine has:")
# coffee_supply = int(input("> "))
# print("Write how many cups of coffee you will need:")
# number_of_coffees = int(input("> "))
#
# water = 200
# milk = 50
# coffee = 15
# # how many coffes can make with supply provided
# n_by_water = water_supply // water
# n_by_milk = milk_supply // milk
# n_by_coffee = coffee_supply // coffee
# # minimum value is amount of coffes coffee machine can make
# n_total = min(n_by_milk, n_by_water, n_by_coffee)
#
# if number_of_coffees == n_total:
#     print("Yes, I can make that amount of coffee")
# elif number_of_coffees > n_total:
#     print("No, I can make only", n_total, "cups of coffee")
# elif number_of_coffees < n_total:
#     print("Yes, I can make that amount of coffee (and even",
#           n_total - number_of_coffees, "more than that)")
# stage 4
state_of_water = 400
state_of_milk = 540
state_of_coffee = 120
state_of_cups = 9
state_of_money = 550


def print_state():
    print("The coffee machine has:")
    print(state_of_water, "of water")
    print(state_of_milk, "of milk")
    print(state_of_coffee, "of coffee beans")
    print(state_of_cups, "of disposable cups")
    print(state_of_money, "of money")
    print()


def change_state(water, milk, coffee, cups, money, operation):
    global state_of_water
    global state_of_milk
    global state_of_coffee
    global state_of_money
    global state_of_cups
    if operation == "+":  # restore supply adding ingredients and disposable cups
        state_of_water += water
        state_of_milk += milk
        state_of_coffee += coffee
        state_of_cups += cups
    elif operation == "-":  # minus state but plus money
        state_of_water -= water
        state_of_milk -= milk
        state_of_coffee -= coffee
        state_of_cups -= cups
        state_of_money += money


def make_coffee(type):
    if type == 1:
        change_state(250, 0, 16, 1, 4, "-")
    elif type == 2:
        change_state(350, 75, 20, 1, 7, "-")
    elif type == 3:
        change_state(200, 100, 12, 1, 6, "-")


def buy_coffee():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = int(input("> "))
    make_coffee(coffee_type)
    print()


def fill():
    print("Write how many ml of water do you want to add:")
    water = int(input("> "))
    print("Write how many ml of milk do you want to add:")
    milk = int(input("> "))
    print("Write how many grams of coffee beans do you want to add:")
    coffee = int(input("> "))
    print("Write how many disposable cups of coffee do you want to add:")
    cups = int(input("> "))
    change_state(water, milk, coffee, cups, 0, "+")


def take():
    global state_of_money
    print("I gave you", state_of_money)
    print()
    state_of_money = 0



print_state()

print("Write action (buy, fill, take):")
action = input("> ")

if action == "buy":
    buy_coffee()
elif action == "fill":
    fill()
elif action == "take":
    take()

print_state()
