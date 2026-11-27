# Food ordering program

tax_rate = 0.08

# menu: item number -> name, price, category
menu = {
    1: {"name": "Cheeseburger", "price": 8.50, "type": "Mains"},
    2: {"name": "Chicken Burger", "price": 8.00, "type": "Mains"},
    3: {"name": "Veggie Burger", "price": 7.50, "type": "Mains"},
    4: {"name": "Margherita Pizza", "price": 10.00, "type": "Mains"},
    5: {"name": "Pepperoni Pizza", "price": 11.50, "type": "Mains"},
    6: {"name": "Spaghetti", "price": 9.50, "type": "Mains"},
    7: {"name": "Chicken Wrap", "price": 7.00, "type": "Mains"},
    8: {"name": "Fish and Chips", "price": 11.00, "type": "Mains"},
    9: {"name": "Fries", "price": 3.50, "type": "Sides"},
    10: {"name": "Onion Rings", "price": 4.00, "type": "Sides"},
    11: {"name": "Side Salad", "price": 3.75, "type": "Sides"},
    12: {"name": "Garlic Bread", "price": 3.50, "type": "Sides"},
    13: {"name": "Chicken Nuggets", "price": 5.00, "type": "Sides"},
    14: {"name": "Soda", "price": 2.00, "type": "Drinks"},
    15: {"name": "Lemonade", "price": 2.50, "type": "Drinks"},
    16: {"name": "Iced Tea", "price": 2.50, "type": "Drinks"},
    17: {"name": "Coffee", "price": 2.75, "type": "Drinks"},
    18: {"name": "Water", "price": 1.00, "type": "Drinks"},
    19: {"name": "Ice Cream", "price": 3.50, "type": "Desserts"},
    20: {"name": "Brownie", "price": 4.00, "type": "Desserts"},
    21: {"name": "Cheesecake", "price": 5.00, "type": "Desserts"},
    22: {"name": "Tomato Soup", "price": 4.50, "type": "Soups"},
    23: {"name": "Chicken Noodle Soup", "price": 5.00, "type": "Soups"},
    24: {"name": "Clam Chowder", "price": 5.50, "type": "Soups"},
    25: {"name": "Caesar Salad", "price": 7.50, "type": "Salads"},
    26: {"name": "Greek Salad", "price": 7.00, "type": "Salads"},
    27: {"name": "Chicken Salad", "price": 8.50, "type": "Salads"},
    28: {"name": "Mini Burger", "price": 5.00, "type": "Kids"},
    29: {"name": "Mac and Cheese", "price": 5.50, "type": "Kids"},
    30: {"name": "Kids Nuggets and Fries", "price": 5.50, "type": "Kids"},
    31: {"name": "Pancakes", "price": 6.50, "type": "Breakfast"},
    32: {"name": "Omelette", "price": 7.00, "type": "Breakfast"},
    33: {"name": "Bacon and Eggs", "price": 7.50, "type": "Breakfast"},
    34: {"name": "French Toast", "price": 6.75, "type": "Breakfast"},
}


def show_menu():
    category = ""
    for number in menu:
        if menu[number]["type"] != category:
            category = menu[number]["type"]
            print("\n" + category)
        print(f"{number}. {menu[number]['name']} - ${menu[number]['price']:.2f}")


def search_menu():
    word = input("Search for: ").lower()
    found = False
    for number in menu:
        if word in menu[number]["name"].lower():
            print(f"{number}. {menu[number]['name']} - ${menu[number]['price']:.2f}")
            found = True
    if found == False:
        print("Nothing found")


def show_cart(cart):
    if len(cart) == 0:
        print("Your cart is empty")
        return
    total = 0
    for number in cart:
        cost = menu[number]["price"] * cart[number]
        print(f"{cart[number]} x {menu[number]['name']} - ${cost:.2f}")
        total = total + cost
    print(f"Subtotal: ${total:.2f}")


def checkout(cart):
    if len(cart) == 0:
        print("Your cart is empty")
        return False

    name = input("Name for the order: ")
    show_cart(cart)

    # work out the price
    subtotal = 0
    for number in cart:
        subtotal = subtotal + menu[number]["price"] * cart[number]
    tax = subtotal * tax_rate

    tip_percent = input("Tip percent (0 for none): ")
    if tip_percent.isdigit():
        tip = subtotal * int(tip_percent) / 100
    else:
        tip = 0
    total = subtotal + tax + tip

    print(f"Tax: ${tax:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"TOTAL: ${total:.2f}")

    file = open("orders.txt", "a")
    file.write("Order for " + name + "\n")
    for number in cart:
        file.write(str(cart[number]) + " x " + menu[number]["name"] + "\n")
    file.write(f"Total: ${total:.2f}\n\n")
    file.close()

    print("Thanks " + name + ", your order is placed!")
    return True


def main():
    cart = {} 
    show_menu()

    while True:
        print("\nType an item number to add it")
        print("m = menu, s = search, v = view cart, r = remove, c = checkout, q = quit")
        choice = input("> ").lower()

        if choice == "q":
            break
        elif choice == "m":
            show_menu()
        elif choice == "s":
            search_menu()
        elif choice == "v":
            show_cart(cart)
        elif choice == "r":
            show_cart(cart)
            number = input("Item number to remove: ")
            if number.isdigit() and int(number) in cart:
                del cart[int(number)]
                print("Removed")
            else:
                print("That isn't in your cart")
        elif choice == "c":
            if checkout(cart):
                break
        elif choice.isdigit() and int(choice) in menu:
            amount = input("How many? ")
            if amount.isdigit():
                number = int(choice)
                if number in cart:
                    cart[number] = cart[number] + int(amount)
                else:
                    cart[number] = int(amount)
                print("Added " + amount + " x " + menu[number]["name"])
            else:
                print("Please enter a number")
        else:
            print("Not a valid choice")

main()