uzbek_food = [
    "Plov",
    "Shashlik",
    "Manti",
    "Lagman",
    "Samsa",
    "Chuchvara"
]


def get_menu_item(food_name):
    return next(
        (food for food in uzbek_food if food.casefold() == food_name.strip().casefold()),
        None,
    )


def find_food(food_name):
    menu_item = get_menu_item(food_name)
    if menu_item:
        return f"{menu_item} is a traditional Uzbek dish."
    else:
        return f"{food_name} is not found in the list of Uzbek dishes."


def select_food():
    print("Available Uzbek dishes:")
    for food in uzbek_food:
        print(f"- {food}")
    user_input = input("Enter the name of the dish you want to check: ")
    result = find_food(user_input)
    print(result)


def add_food_in_cart(cart, food_name):
    menu_item = get_menu_item(food_name)
    if menu_item:
        cart.append(menu_item)
        return f"{menu_item} has been added to your cart."
    else:
        return f"{food_name} is not available in the menu."


def view_cart(cart):
    if cart:
        print("Your cart contains the following dishes:")
        for item in cart:
            print(f"- {item}")
    else:
        print("Your cart is empty.")


def remove_food_from_cart(cart, food_name):
    menu_item = get_menu_item(food_name)
    if menu_item in cart:
        cart.remove(menu_item)
        return f"{menu_item} has been removed from your cart."
    else:
        return f"{food_name} is not in your cart."


def order_food(cart):
    if cart:
        address = input("Enter your delivery address: ").strip()
        phone = input("Enter your contact phone number: ").strip()
        if not address or not phone:
            return "Delivery address and phone number are required. Your order was not placed."

        order_details = [
            "Delivery order prepared (demo only).",
            "Dishes:",
            *(f"- {item}" for item in cart),
            f"Delivery address: {address}",
            f"Contact phone: {phone}",
        ]
        cart.clear()
        return "\n".join(order_details)
    else:
        return "Your cart is empty. Please add some dishes before ordering."


def main():
    cart = []
    while True:
        print("\nMenu:")
        print("1. View dishes and check availability")
        print("2. Add dish to cart")
        print("3. View cart")
        print("4. Remove dish from cart")
        print("5. Place delivery order")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            select_food()
        elif choice == "2":
            food_name = input("Enter the name of the dish to add to cart: ")
            result = add_food_in_cart(cart, food_name)
            print(result)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            food_name = input("Enter the name of the dish to remove from cart: ")
            result = remove_food_from_cart(cart, food_name)
            print(result)
        elif choice == "5":
            result = order_food(cart)
            print(result)
        elif choice == "6":
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    