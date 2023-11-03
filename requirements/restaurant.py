class Restaurant:

    @staticmethod
    def register_restaurant() -> dict | None:
        name = input("Enter the name of the restaurant: ")
        owner = input("Enter the name of the owner: ")
        payment_information = []
        payment_information.append(input("Enter debit card type: "))
        payment_information.append(input("Enter debit card number: "))
        payment_information.append(input("Enter debit card expiration date: "))
        payment_information.append(input("Enter debit card security code: "))
        location = input("Enter the address of the restaurant: ")
        phone = input("Enter the phone number of the restaurant: ")
        notDone = True
        print()
        menu = {}
        while notDone:
            menuItem = input("Enter a menu item: ")
            price = input("Enter item price: ")

            if price.replace(".", "").isnumeric():
                price = float(price)
                menu[menuItem] = price

                finished = input("Do you have anymore items to add? (Y/N)")
                if finished[0].upper() != "Y":
                    notDone = False
            else:
                print("Invalid price value")

        print()

        if len(payment_information) != 4:
            print("Invalid input. Please try again.")
            return None

        elif name and owner and payment_information and location and phone:
            restaurant = {
                "restaurant_name": name,
                "restaurant_info": {
                    "owner": owner,
                    "phone_number": phone,
                    "home_address": location
                },
                "direct_deposit_info": {
                    "card_type": payment_information[0],
                    "card_numbers": payment_information[1],
                    "expiry_date": payment_information[2],
                    "cvv": payment_information[3]
                },
                "order_queue": {
                    "current_orders": {},
                    "finished_orders": {}
                },
                "menu": menu
            }

            return restaurant
        else:
            print("Missing information!")
            return None

    @staticmethod
    def get_restaurant_order_queue(restaurant: dict) -> None:
        print()
        print(f"\t\t{restaurant['restaurant_name']}: Current Orders")
        print("=========================================================")
        for key in restaurant['order_queue']['current_orders']:
            print(f"\t\t{key}: {restaurant['order_queue']['current_orders'][key]}")
        print("=========================================================")

    @staticmethod
    def get_restauraunt_menu(restaurant: dict) -> None:
        print()
        print(f"\t\t{restaurant['restaurant_name']} Menu:")
        print("=========================================================")
        for key in restaurant["menu"]:
            print(f"\t\t{key}: {restaurant['menu'][key]}")
        print("=========================================================")

    @staticmethod
    def get_restaurants(restaurants) -> None:
        print()
        print("=========================================================")
        for key in restaurants:
            print(f"\t\t{key['restaurant_name']}")
        print("=========================================================")

    @staticmethod
    def remove_restaurant_order(restaurant: dict, id: int, reason: str) -> bool:
        return restaurant["order_queue"]["current_orders"].get(str(id)) != None

