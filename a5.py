
def logo():
    print(r"""
         ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
        ||B |||o |||o |||k |||i |||n |||g |||B |||e |||s |||t ||
        ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
        |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\| 
        """)

# Login page
def login(valid_id_pw):
    logo()
    print("[Login]")
    print("Type in your ID and Password.\n")
    
    while True:
        user_id = input("ID: ")
        user_pw = input("Password: ")
        if user_id in valid_id_pw and user_pw == valid_id_pw[user_id]:
            break
        else:
            print("Invalid ID or Password. Try again.")
    return True

def main_page():
    logo()
    print("[Main Page]")
    while True:
        print("Store Registration: For store owners, register your own store. (Requires the details of your store)")
        print("Store Search: For customers, search the stores that match your keyword.")
        main_choice = input("\nFor Store Registration, Type 1."
                            "\nFor Store Search, Type 2."
                            "\n").strip()
        if main_choice == "1" or main_choice == "2":
            break
        else:
            print("Invalid input. Try again.")
    return main_choice

def store_registration(store_dict):
    while True:
        print("\nType in Your Store Name.")

        store_name = input("\nStore Name: ")

        if store_name.strip() == "":
            print("Invalid input. Try again.")
        elif store_name in store_dict:
            print("Store name already exists. Try again.")
        else:
            break

    return store_name

def store_registration_alert():
    while True:
        print('\n[Alert]'
              '\nAre you sure?'
              '\nClicking "Submit" will make your store visible to all users.'
              '\nIs this really what you want to do?')
        alert_answer = input('\nType 1 to say Yes.'
                             '\nType 2 to say No.'
                             '\n').strip()
        if alert_answer == "1" or alert_answer == "2":
            break
    return alert_answer

def store_details():
    print("\nType in Your Store Details.\n")

    while True:
        user_phone = input("Phone Number: ")
        if user_phone.replace("-", "").isdigit() and user_phone != "":
            break
        else:
            print("Invalid input. Try again.")
    while True:
        user_email = input("Email: [Email ID] @ [Select Email domain]"
                                 "\nType in Email ID part: ")
        user_email += "@"
        user_email_select = input("\nSelect Email domain: "
                                   "\nType 1 to select gmail.com"
                                   "\nType 2 to select outlook.com"
                                   "\nType 3 to select icloud.com"
                                   "\nType 4 to Enter manually"
                                   "\n").strip()
        if user_email_select == "1":
            user_email += "gmail.com"
            break
        elif user_email_select == "2":
            user_email += "outlook.com"
            break
        elif user_email_select == "3":
            user_email += "icloud.com"
            break
        elif user_email_select == "4":
            user_email += input("Enter Email domain manually")
            break
        else:
            print("Invalid input. Try again.")

    while True:
        user_hours = input("\nBusiness hours: ")
        if user_hours.strip() != "":
            break
        else:
            print("Invalid input. Try again.")

    while True:
        user_address = input("\nAddress: ")
        if user_address.strip() != "":
            break
        else:
            print("Invalid input. Try again.")

    while True:
        user_menu = input("\nMenu: ")
        if user_menu.strip() != "":
            break
        else:
            print("Invalid input. Try again.")

    while True:
        user_description = input("\nDescription: ")
        if user_description.strip() != "":
            break
        else:
            print("Invalid input. Try again.")

    return user_phone, user_email, user_hours, user_address, user_menu, user_description

def store_search():
    print("\nPlease enter a keyword for store name search.")
    user_search = input("\nSearch: ").strip().lower()

    return user_search

def search_results(user_search, store_dict):
    while True:
        num_printed = 0
        display_type = input("\nInstructions:"
                             "\nType 1 to see the Top 3 results."
                             "\nType 2 to see All results."
                             "\nType 3 to return to the Buttons menu."
                             "\n").strip()
        if display_type == "1":
            print("\nResults:")
            for store_name in store_dict:
                if num_printed == 3:
                    break
                if user_search in store_name.lower():
                    print(store_name)
                    num_printed += 1
        elif display_type == "2":
            print("\nResults:")
            for store_name in store_dict:
                if user_search in store_name.lower():
                    print(store_name)
                    num_printed += 1
        elif display_type == "3":
            print("\n")
            break
        else:
            print("Invalid input. Try again.")


def button_only_home():
    while True:
        button = input("Buttons:"
                       "\nType 'H' to go to the Main Page."
                       "\nType 'C' to continue to this page."
                       "\n"
                       "\n").strip().upper()
        if button == "H":
            return button
        elif button == "C":
            return button
        else:
            print("Invalid input. Try again.")


def button_home_back():
    while True:
        button = input("Buttons:"
                       "\nType 'H' to go to the Main Page."
                       "\nType 'B' to go back."
                       "\nType 'C' to continue to this page."
                       "\n"
                       "\n").strip().upper()
        if button == "H":
            return button
        elif button == "B":
            return button
        elif button == "C":
            return button
        else:
            print("Invalid input. Try again.")

def line():
    print("\n-------------------------------------------------------------------\n")

if __name__ == "__main__":
    valid_id_pw = {"id_sample": "pw_sample"}
    store_dict = {"Store A": {"phone_number": "000-000-0000",
                              "email": "storeA@gmail.com",
                              "business_hours": "12pm-2pm"},
                  "Store B": {},
                  "Store C": {},
                  "Store D": {},
                  "Store E": {}}

    current_page = "Login"
    line()
    if login(valid_id_pw):
        current_page = "Main"

    while True:
        # Main page
        if current_page == "Main":
            line()
            main_choice = main_page()
            if main_choice == "1":
                current_page = "Register"
            elif main_choice == "2":
                current_page = "Search"


        # Store Registration page
        elif current_page == "Register":
            line()
            logo()
            print("[Store Registration]")
            button_press = button_only_home()
            if button_press == "H":
                current_page = "Main"
                continue
            else:
                store_name = store_registration(store_dict)
                line()
                alert_answer = store_registration_alert()
                if alert_answer == "1":
                    current_page = "Register_details"

                elif alert_answer == "2":
                    current_page = "Register"

        # Store Details page
        elif current_page == "Register_details":
            line()
            logo()
            print("\n[Store Details]")
            button_press = button_home_back()
            if button_press == "H":
                current_page = "Main"
                continue
            elif button_press == "B":
                current_page = "Register"
                continue
            else:
                user_phone, user_email, user_hours, user_address, user_menu, user_description = store_details()
                store_dict[store_name] = {}
                store_dict[store_name]["phone_number"] = user_phone
                store_dict[store_name]["email"] = user_email
                store_dict[store_name]["business_hours"] = user_hours
                store_dict[store_name]["address"] = user_address
                store_dict[store_name]["menu"] = user_menu
                store_dict[store_name]["description"] = user_description

                print("\nYour store is now registered!")
                current_page = "Main"

        # Store Search page
        elif current_page == "Search":
            line()
            logo()
            print("\n[Store Search]")
            button_press = button_only_home()
            if button_press == "H":
                current_page = "Main"
                continue
            else:
                user_search = store_search()
                current_page = "Search_results"

        # Search Results page
        elif current_page == "Search_results":
            line()
            logo()
            print("\n[Search Results]")
            search_results(user_search, store_dict)
            button_press = button_home_back()
            if button_press == "H":
                current_page = "Main"
            elif button_press == "B":
                current_page = "Search"
            else:
                continue








