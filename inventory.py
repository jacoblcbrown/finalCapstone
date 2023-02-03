# ==================== Compulsory Task ====================

# ========== Imports ==========
from tabulate import tabulate


# ========== Classes ==========
# This class is used to describe the shoes the store stocks and all of their respective information: country, code,
# product, cost and quantity.
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        str_output = (f"COUNTRY: {self.country}\n"
                      f"CODE: {self.code}\n"
                      f"PRODUCT: {self.product}\n"
                      f"COST: {self.cost}\n"
                      f"QUANTITY: {self.quantity}\n")

        return str_output


# This class is used to represent the shoes in stock as a group. Information relating to the group as a whole is found
# using it's methods.
class ShoeStock:
    def __init__(self, shoe_list):
        self.shoe_list = shoe_list

    def get_min_quantity(self):
        min_qty = min(self.shoe_list, key=lambda shoe: shoe.quantity)

        return min_qty

    def get_max_quantity(self):
        max_qty = max(self.shoe_list, key=lambda shoe: shoe.quantity)

        return max_qty

    def get_search_result(self):
        search_code = input("Please enter the product code: ").upper()
        search_results = [shoe for shoe in self.shoe_list if shoe.code == search_code][0]

        return search_results

    def get_value_per_item(self):
        value_results = [[shoe.code, shoe.product, shoe.get_cost() * shoe.get_quantity()]
                         for shoe in self.shoe_list]

        return value_results


#========== Functions ==========
# This function opens the file 'inventory.txt', reads the data from it and then create a shoe object for each row.
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as shoe_file:

            count_for_heading_skip = 1

            for line in shoe_file:
                line = line.strip("\n").split(",")

                if count_for_heading_skip > 1:

                    line = Shoe(line[0], line[1], line[2], int(line[3]), int(line[4]))
                    shoe_list.append(line)

                count_for_heading_skip += 1

        return shoe_list

    except FileNotFoundError:
        print("File not found. Please make sure your program references the correct inventory file and try again.")
        exit()


# This function lets the user add a new shoe to the list.
def capture_shoes():
    print("Please enter the following information: ")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = int(input("Cost: "))
    quantity = int(input("Quantity: "))

    shoe_list.append(Shoe(country, code, product, cost, quantity))

    print("Shoe successfully added.")


# This function lets the user view all shoes in the list.
def view_all():
    table = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
    print(tabulate(table, headers=['Country', 'Code', 'Product', 'Cost', 'Quantity']))
    print()  # Spacing.


# This function finds the product with the lowest quantity and allows the user to add more stock.
def re_stock():
    min_shoe = ShoeStock(shoe_list).get_min_quantity()

    print(f"The shoe with the lowest quantity is:-\n"
          f"{min_shoe}")

    while True:
        menu = input("Would you like to restock?\n"
                     "Y - yes\n"
                     "N  - no\n"
                     "\nEnter here: ").lower()

        if menu == "y":
            restock_qty = int(input("\nHow many units would you like you to order: "))

            min_shoe.quantity += restock_qty

            print(f"\nShoe successfully restocked. Total units updated to {restock_qty}.")

            break

        elif menu == "n":
            break

        else:
            print("Input not recognised. Please try again.\n")  # Input validation check.


# This function searches for a shoe based on its product code. It is then printed out.
def search_shoe():
    shoe_info = ShoeStock(shoe_list).get_search_result()

    print(f"This code returns the following shoe:-\n"
          f"{shoe_info}")


# This function calculates the value of each shoe and prints out the results in the table. Value is defined as cost *
# quantity.
def value_per_item():
    shoe_values = ShoeStock(shoe_list).get_value_per_item()

    print(tabulate(shoe_values, headers=['Code', 'Product', 'Value']))


# This function finds the product with the highest quantity and allows the user to apply a sale to it.
def highest_qty():
    pass

    max_shoe = ShoeStock(shoe_list).get_max_quantity()

    print(f"The shoe with the highest quantity is:-\n"
          f"{max_shoe}\n")

    while True:
        menu = input("Would you like to mark it for sale?\n"
                     "Y - yes\n"
                     "N  - no\n"
                     "\nEnter here: ").lower()

        if menu == "y":
            sale_cost_pc = int(input("\nWhat sale percentage would you like to apply? (e.g. 10%, 50%): "))

            max_shoe.cost = round(max_shoe.cost * ((100 - sale_cost_pc)/100))

            print(f"\nShoe successfully put on sale. Cost updated to {max_shoe.cost}.\n")
            break

        elif menu == "n":
            break

        else:
            print("Input not recognised. Please try again.\n")  # Input validation check.


# ========== Variables ==========
# The list will be used to store a list of objects of shoes.
shoe_list = []

# ========== Main Program ==========
read_shoes_data()

while True:
    # User menu.
    menu = input("==========================================\n"
                 "                 MAIN MENU\n"
                 "==========================================\n"
                 "Select one of the following options below:\n"
                 "a  - Add shoe\n"
                 "r - Restock shoe\n"
                 "s - Search shoe\n"
                 "v - View all shoes\n"
                 "t - Total value of each shoe\n"
                 "q - Highest quantity shoe\n"
                 "x  - Exit\n"
                 "\nEnter here: ").lower()

    if menu == "a":
        capture_shoes()

    elif menu == "r":
        re_stock()

    elif menu == "s":
        search_shoe()

    elif menu == "v":
        view_all()

    elif menu == "t":
        value_per_item()

    elif menu == "q":
        highest_qty()

    elif menu == "x":
        exit()

    else:
        print("Input not recognised. Please try again.")  # Input validation check.
