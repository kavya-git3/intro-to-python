import datetime
Menu = {
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 100,
  },
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 75,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 100,
  },
}

profit = 0
resources = {
  "water": 1000,
  "milk": 500,
  "coffee": 100,
}


def check_resources(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"Sorry there is not enough {item}")
      return False
  return True


def process_coins():
  print("Please insert coins.")
  total = 0
  coins_five = int(input("How many 5rs coin?:"))
  coins_Ten = int(input("How many 10rs coin?:"))
  coins_Twenty = int(input("How many 20rs coin?:"))
  total = coins_five * 5 + coins_Ten * 10 + coins_Twenty * 20
  return total


def is_payment_successful(money_received, coffee_cost):
  if money_received >= coffee_cost:
    global profit
    profit += coffee_cost
    change = money_received - coffee_cost
    print(f"Here is your Rs{change} in change.")
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(coffee_name, coffee_ingredients):
  for item in coffee_ingredients:
    resources[item] -= coffee_ingredients[item]
  print(f"Here is your {coffee_name} ....Enjoy!!")

def display_menu_and_date():
    current_date = datetime.date.today()
    print(f"Welcome to the Coffee Machine!")
    print(f"Today's Date: {current_date}")
    print("\nMenu:")
    for coffee in Menu:
        cost = Menu[coffee]["cost"]
        print(f"{coffee.capitalize()} - Rs{cost}")
    print("\nType 'report' to see resource status.")
    print("Type 'off' to turn off the machine.")
  

is_on = True
while is_on:
  display_menu_and_date()
  choice = input(
    "What would you like to have? (latte/espresso/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: Rs {profit}")
  else:
    coffee_type = Menu[
      choice]  # Retrieve the selected coffee type from the menu
    print(coffee_type)
    if check_resources(coffee_type['ingredients']):
      payment = process_coins()
      if is_payment_successful(payment, coffee_type['cost']):
        make_coffee(choice, coffee_type['ingredients'])
