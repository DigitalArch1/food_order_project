# food ordering program

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
}


def show_menu():
    print()
    print("MENU")
    last_type = ""
    for num in menu:
        item = menu[num]
        if item["type"] != last_type:
            print()
            print(item["type"])
            last_type = item["type"]
        print(num, "-", item["name"], "$" + format(item["price"], ".2f"))


def add_item(cart, num, amount):
    if num not in menu:
        print("not on the menu")
        return
    if num in cart:
        cart[num] = cart[num] + amount
    else:
        cart[num] = amount
    print("added", amount, menu[num]["name"])


def get_total(cart):
    total = 0
    for num in cart:
        total = total + menu[num]["price"] * cart[num]
    return total


def show_cart(cart):
    print()
    print("YOUR ORDER")
    if len(cart) == 0:
        print("nothing in your cart")
        return
    for num in cart:
        print(cart[num], "x", menu[num]["name"])
    print("total: $" + format(get_total(cart), ".2f"))


def main():
    cart = {}
    while True:
        show_menu()
        choice = input("\nPick a number, c to checkout, q to quit: ")

        if choice == "q":
            break
        elif choice == "c":
            show_cart(cart)
            print("thanks!")
            break
        elif choice.isdigit():
            amount = input("How many? ")
            if amount.isdigit():
                add_item(cart, int(choice), int(amount))
            else:
                add_item(cart, int(choice), 1)
        else:
            print("not a valid choice")


main()