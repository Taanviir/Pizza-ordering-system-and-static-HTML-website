"""
Pizza Ordering System
-----------------------
Osama Elshareef
Tanvir Ahmed
----------------------
"""

# welcome() will display the welcome screen and get the input from the user.
# In case of wrong character being entered by the user, the while loop will show an error message and ask the user to type again.
def welcome():
    print("\n" + "-"*100)
    print("🍕 Welcome to Pizza Way! 🍕".center(100))
    print("\n\t\tPlease select one of the following options (type the number only!)\n1. Menu \n2. Order \n3. Exit")
    while True:
        x = input("").strip()
        if x == "1":
            print("\n" + "-"*60)
            menu()
            break
        elif x == "2":
            print("\n" + "-"*60)
            order()
            break
        elif x == "3":
            break
        else:
            print("Error! Please type the number only.\n")
            continue

pizza_type = ["1- Margherita", "2- Neopolitan", "3- Vegeterian", "4- Pepperoni"]
small_price = [30, 32, 30, 35]
medium_price = [40, 42, 40, 45]
large_price = [50, 52, 50, 55]
# Menu() is used to display the menu. It then asks the user if they want to proceed to ordering directly or return to the 
# main screen.
def menu():
    print("      Pizza        Small           Medium            Large")
    print("-"*60)
    for _ in range(4):
        print(pizza_type[_] +"\t   AED "+  str(small_price[_]) + "\t   AED " + str(medium_price[_]) +"\t     AED " + 
        str(large_price[_]))
    print("-"*60)
    print("If you want extra toppings, the available ones are Olives 🫒, Mushrooms 🍄, Tomatoes 🍅 and\n Peppers 🫑. " + 
    "\n\n*Please note that only the first 3 toppings are free and the any additional toppings will cost\n AED 3 each.*")
    print("-"*100)
    
    while True:
        print("Would you like to order or return back to the previous page? (Type 1 to proceed or Type 2 to return)")
        y = input().lower().strip()

        if y == "1":
            print("\n" + "-"*100)
            order()
            break
        elif y == "2":
            print("\n" + "-"*100)
            welcome()
            break
        else:
            print("Error! Please type only 1 or 2!\n")
            continue

ordered_pizza = []
order_price = []
ordered_size = []
# Order() is used to make orders. It shows the available pizzas and then asks the user to choose one, then asks the user about
# toppings and finally asks if the user wants to order another pizza from which a loop is triggered.
def order():
    # Pizza quantity asked and only integers are accepted by program
    print("Here are the available pizzas:")
    for _ in range(4):
        print(pizza_type[_])
    valid = False
    while not valid:
        try:
            quantity = int(input("\nHow many pizzas would you like? (Type the number)\n").strip())
            valid = True
        except ValueError:
            print("Error! Please only enter the number!\n")
    
    x = 0
    while x < quantity:
        # Available pizzas shown and order taken
        print("\n" + "-"*60)
        print("Here are the available pizzas:")
        for _ in range(4):
            print(pizza_type[_])
        valid = False
        while not valid:
            try:
                pizza_code = int(input("\nWhich pizza would you like? (Type the number next to it)\n").strip()) - 1
                valid = True
            except ValueError:
                print("Error! Please only enter the number!\n")
        print("\n" + "-"*60)

        # Appending the ordered pizza
        while 0 <= pizza_code <= 3:
            if pizza_code == 0:
                ordered_pizza.append("Margherita")
                break
            elif pizza_code == 1:
                ordered_pizza.append("Neopolitan")
                break
            elif pizza_code == 2:
                ordered_pizza.append("Vegeterian")
                break
            elif pizza_code == 3:
                ordered_pizza.append("Pepperoni")
                break
            else:
                break

        # Shows the pizza that the user has selected
        for _ in range(1):
            print(str(pizza_type[pizza_code]) + "\t   Small = AED " +  str(small_price[pizza_code]) + "\t   Medium = AED "
            + str(medium_price[pizza_code]) + "\t   Large = AED " + str(large_price[pizza_code]))

        # Size-based prices
        while True:
            preferred_size = input("What size would you like? (Type S, M or L)\n").upper().strip()
            if preferred_size == "S":
                order_price.append(small_price[pizza_code])
                ordered_size.append("Small")
                break
            elif preferred_size == "M":
                order_price.append(medium_price[pizza_code])
                ordered_size.append("Medium")
                break
            elif preferred_size == "L":
                order_price.append(large_price[pizza_code])
                ordered_size.append("Large")
                break
            else:
                print("Error! Please type the correct letter!")
                continue
        toppings()
        x += 1
    invoice()

extra_toppings = []
toppings_price = []
t_count = []
# Toppings function
def toppings():
    while True:
        print("\nDo you want to add any extra toppings (the first 3 are free)? (Type yes/no)")
        q = input("").lower().strip()
        i = 0
        if q == "yes":
            # free toppings only
            print("\nThe available toppings are Olives 🫒 , Mushrooms 🍄, Tomatoes 🍅 and Peppers 🫑 .")
            valid = False
            while not valid:
                try:
                    num_of_toppings = int(input("How many toppings would you like? "))
                    valid = True
                except ValueError:
                    print("Error! Please only enter the number!\n")
            t_count.append(num_of_toppings)

            if num_of_toppings <= 3:
                while i < num_of_toppings:
                    print("\nThis topping will be free.")
                    x = input("What topping would you like? (Type O, M, T, or P)\n").upper().strip()
                    if x == "O" or x == "M" or x == "T" or x == "P":
                        name = topping_names(x)
                        extra_toppings.append(name)
                        toppings_price.append(0)
                        i += 1
                    else:
                        print("Error! Please type the correct number!\n")
                        continue
            else:
                # free and paid toppings
                while i < 3:
                    print("\nThis topping will be free.")
                    x = input("What topping would you like? (Type O, M, T, or P)\n").upper().strip()
                    if x == "O" or x == "M" or x == "T" or x == "P":
                        name = topping_names(x)
                        extra_toppings.append(name)
                        toppings_price.append(0)
                        i += 1
                    else:
                        print("Error! Please type the correct number!\n")
                        continue
                i = 0
                paid = num_of_toppings - 3
                while i < paid:
                    print("\nEvery topping from now will cost an additional AED 3.")
                    y = input("Which topping would you like to add more?\n").upper().strip()
                    name = topping_names(y)
                    extra_toppings.append(name)
                    toppings_price.append(3)
                    i += 1
            break
        elif q == "no":
            break
        else:
            print("Error! Please type yes or no only!")
            continue

# This function returns the names of the toppings
def topping_names(topping_initial):
    if topping_initial == "O":
        return "Olives"
    elif topping_initial == "M":
        return "Mushrooms"
    elif topping_initial == "T":
        return "Tomatoes"
    elif topping_initial == "P":
        return "Peppers"

# Printing the invoice
def invoice():
    Total_price = 0
    for i in order_price:
        Total_price += i
    for j in toppings_price:
        Total_price += j

    username = input("\nPlease give us your name before we print the receipt: ").strip().title()
    print("\n" + "*"*50 + f"\n\t           🍕 Pizza Way 🍕")
    print(f"Invoice for {username}\n".center(55))
    print("Pizza Name:			      Price:")
    for x in range(0, len(ordered_pizza)):
        print(f"{ordered_pizza[x]} ({ordered_size[x]}) 	              AED {order_price[x]}")
        if len(t_count) > 0:
            print("\n\tToppings:")
            for _ in range(0, t_count[x]):
                print("{:>20} {:>20} {:}".format(extra_toppings[0], "AED", toppings_price[0]))
                extra_toppings.remove(extra_toppings[0])
                toppings_price.remove(toppings_price[0])
            print()

    print("-"*50 + "\n        Total to be paid:             AED {:}".format(Total_price))
    print("\n     Thank your for ordering from Pizza Way :)\n" +"*"*50)

    while True:
        back = input("Type 1 if you want to go back to main screen. ").lower().strip()
        if back == "1":
            welcome()
            break
        else:
            print("Error please type yes or no only!\n")
welcome()