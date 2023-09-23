import sys

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

updated_resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}


def report_stats():
    water_status = resources["water"]
    milk_status = resources["milk"]
    coffee_status = resources["coffee"]

    if resources["money"] != 0:
        money_status = resources["money"]
        print(f"Water: {water_status} ml\nMilk: {milk_status} ml\nCoffee: {coffee_status} \nMoney: {money_status}")
        return
    else:
        print(f"Water: {water_status} ml\nMilk: {milk_status} ml\nCoffee: {coffee_status} \n")
        return


def coffee_selection(drink):
    if drink == "espresso":
        print("You pick espresso")
        return
    elif drink == "latte":
        print("You picked Latte")
        report_stats()
        return
    elif drink == "cappuccino":
        print("You picked cappuccino")
        return
    elif drink == "off":
        print("Maintenance have began. Machine is turning off.")
        sys.exit()
    else:
        input("Please choose from following selection espresso/latte/cappuccino \n").lower()
        return


def coin_total(quarter, nickel, dime, penny):
    quart_value = float(.25)
    quarter_total = quart_value * quarter

    dime_value = float(.10)
    dime_total = dime_value * dime

    nickel_value = float(.5)
    nickel_total = nickel_value * nickel

    penny_value = float(.1)
    penny_total = penny_value * penny

    coin_sum = quarter_total + dime_total + nickel_total + penny_total
    return coin_sum


def restart():
    turn_off = False

    while not turn_off:
        print_report = input("Do you want to print a status report? Yes or No \n").lower()

        if print_report == 'yes':
            print(report_stats())

        user_drink = input("What would you like? (espresso/latte/cappuccino): \n").lower()

        coffee_selection(user_drink)

        # Insert coins for drink

        print("Please insert coins. Quarters, Nickels, Dimes, and Pennies \n")

        quarters = float(input("How many quarters? "))
        nickels = float(input("How many Nickels? "))
        dimes = float(input("How many dimes? "))
        pennies = float(input("How many pennies? "))

        coin_total_sum = coin_total(quarters, nickels, dimes, pennies)

        print(coin_total_sum)

        # Set refund coins to 0
        refund_coins = 0

        # Check the drink resources
        if user_drink == "latte":
            if float(resources["water"]) > float(MENU["latte"]["ingredients"]["water"]):
                print("You have enough water")
                if float(resources["milk"]) > float(MENU["latte"]["ingredients"]["milk"]):
                    print("You have enough milk.")
                    if float(resources["coffee"]) > float(MENU["latte"]["ingredients"]["coffee"]):
                        print("You have enough coffee. ")
                        print("We are making your Latte. Please wait.....")

                        # subtract the resources from order
                        resources["water"] = float(resources["water"]) - float(MENU["latte"]["ingredients"]["water"])
                        resources["milk"] = float(resources["milk"]) - float(MENU["latte"]["ingredients"]["milk"])
                        resources["coffee"] = float(resources["coffee"]) - float(MENU["latte"]["ingredients"]["coffee"])

                        # Subtract coins from coffee price
                        if coin_total_sum >= 2.50:
                            latte_price = float(MENU["latte"]["cost"])
                            print(f"Latte Price: {latte_price} you gave {coin_total_sum}")
                            order = coin_total_sum - float(MENU["latte"]["cost"])
                            resources["money"] = 2.50

                            # Refunded money if over drink price
                            if coin_total_sum > 2.50:
                                refund_coins = coin_total_sum - 2.50
                                print(f"Too much money inserted. Refunded $ {refund_coins}")
                            print(resources)
                            print(f"Here is your {user_drink}. Enjoy! \n")

                            another_coffee = input("Would you like to order another drink? Yes or No").lower()

                            if another_coffee == "yes":
                                turn_off = False
                            elif another_coffee == "no":
                                turn_off = True

                        elif coin_total_sum < 2.49:
                            refund_coins = coin_total_sum
                            print(f"“Sorry that's not enough money. Money refunded $ {refund_coins}.")
                        # turn_off = False
                    else:
                        print("Sorry, not enough coffee.")
                else:
                    print("Sorry, not enough milk")
            else:
                print("Sorry, not enough water")
        elif user_drink == "espresso":
            if float(resources["water"]) > float(MENU["espresso"]["ingredients"]["water"]):
                print("You have enough water")
                if float(resources["coffee"]) > float(MENU["espresso"]["ingredients"]["coffee"]):
                    print("You have enough coffee. ")
                    print("We are making your Latte. Please wait.....")

                    # subtract the resources from order
                    resources["water"] = float(resources["water"]) - float(MENU["espresso"]["ingredients"]["water"])
                    resources["coffee"] = float(resources["coffee"]) - float(MENU["espresso"]["ingredients"]["coffee"])

                    # Subtract coins from coffee price
                    if coin_total_sum >= 1.50:
                        espresso_price = float(MENU["espresso"]["cost"])
                        print(f"{user_drink} Price: {espresso_price} you gave {coin_total_sum}")
                        order = coin_total_sum - float(MENU["espresso"]["cost"])
                        resources["money"] = 1.50

                        # Refunded money if over drink price
                        if coin_total_sum > 1.50:
                            refund_coins = coin_total_sum - 1.50
                            print(f"Too much money inserted. Refunded $ {refund_coins}")
                        print(resources)
                        print(f"Here is your {user_drink}. Enjoy! \n")

                        another_coffee = input("Would you like to order another drink? Yes or No").lower()

                        if another_coffee == "yes":
                            turn_off = False
                        elif another_coffee == "no":
                            turn_off = True

                    elif coin_total_sum <= 1.49:
                        refund_coins = coin_total_sum
                        print(f"“Sorry that's not enough money. Money refunded $ {refund_coins}.")
                    # turn_off = False
                else:
                    print("Sorry, not enough coffee.")
            else:
                print("Sorry, not enough water")
        elif user_drink == "cappuccino":
            if float(resources["water"]) > float(MENU["cappuccino"]["ingredients"]["water"]):
                print("You have enough water")
                if float(resources["milk"]) > float(MENU["cappuccino"]["ingredients"]["milk"]):
                    print("You have enough milk.")
                    if float(resources["coffee"]) > float(MENU["cappuccino"]["ingredients"]["coffee"]):
                        print("You have enough coffee. ")
                        print("We are making your Latte. Please wait.....")

                        # subtract the resources from order
                        resources["water"] = float(resources["water"]) - float(MENU["cappuccino"]["ingredients"]["water"])
                        resources["milk"] = float(resources["milk"]) - float(MENU["cappuccino"]["ingredients"]["milk"])
                        resources["coffee"] = float(resources["coffee"]) - float(MENU["cappuccino"]["ingredients"]["coffee"])

                        # Subtract coins from coffee price
                        if coin_total_sum >= 3.00:
                            cappuccino_price = float(MENU["latte"]["cost"])
                            print(f"Latte Price: {cappuccino_price} you gave {coin_total_sum}")
                            order = coin_total_sum - float(MENU["cappuccino"]["cost"])
                            resources["money"] = 3.00

                            # Refunded money if over drink price
                            if coin_total_sum > 3.00:
                                refund_coins = coin_total_sum - 3.00
                                print(f"Too much money inserted. Refunded $ {refund_coins}")
                            print(resources)
                            print(f"Here is your {user_drink}. Enjoy! \n")

                            another_coffee = input("Would you like to order another drink? Yes or No").lower()

                            if another_coffee == "yes":
                                turn_off = False
                            elif another_coffee == "no":
                                turn_off = True

                        elif coin_total_sum <= 2.99:
                            refund_coins = coin_total_sum
                            print(f"“Sorry that's not enough money. Money refunded $ {refund_coins}.")
                        # turn_off = False
                    else:
                        print("Sorry, not enough coffee.")
                else:
                    print("Sorry, not enough milk")
            else:
                print("Sorry, not enough water")


restart()