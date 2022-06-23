
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_drink(drink):
    ings = MENU[drink]["ingredients"]
    cost = MENU[drink]["cost"]
    for x in ings:
        if x in resources:
            if resources[x] < ings[x]:
                print (f"There's not enough {x}")
            else:
                print(f"Great we have enough {x}")

def insert_money(drink):
    cost = MENU[drink]["cost"]
    total = 0
    print (f"It costs {cost}")
    total = int(input("how many quarters? ")) * 0.20
    print(f"That's {total}")
    total += int(input("how many nickels? ")) * 0.05
    print(f"That's {total}")
    total += int(input("how many dimes? ")) * 0.10
    print(f"That's {total}")
    total += int(input("how many pennies? ")) * 0.01
    if total < cost:
        print("Sorry that's not enough money")
    else:
        change = total - cost
        resources["money"] += cost
        print(f"Here is your {drink} and here's ${change} in change")

def deduct_ingredients(drink):
    ings = MENU[drink]["ingredients"]
    for x in ings:
        resources[x] -= ings[x]

def make_drink(drink):
    check_drink(drink)
    insert_money(drink)
    deduct_ingredients(drink)

machine = True
def what_like():
    while machine is True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            report()
        elif order == "off":
            break
        else:
            make_drink(order)
            print (report())

# TODO Set up report reading what's left.

def report():
    for x in resources:
        print(f"{x}: {resources[x]}")


# TODO Coins function. Insert coins for that drink. Check coins. Work out change.
# TODO Deduct function takes resources from the machine.
# TODO Back in the drink function return.
# TODO Give them the drink. And go back to beginning.

what_like()