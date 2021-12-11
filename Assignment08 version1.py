# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# GGornalusse,12.5.2021,Modified initial code and created version 1
# GGornalusse, 12.8.2021,Modified version 1 and created version 2
# ------------------------------------------------------------------------ #


# Data -------------------------------------------------------------------- #
# Declare variables and constants

file_name = "List of Products and Prices.txt"  # The name of the data file
list_of_product_objects = []  # Captures the data from a file into a dic and from a dictionary to a list of dic rows
objfile = None  # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Product,Price}
choice = ""  # Captures the user option selection
product_name = ""  # Captures the user product's name
product_price = ""  # Captures the user product's price


# Class Product

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name

        product_price: (float) with the products's standard price
    methods:
        the string method (__str__), which returns a string of the product_name comma-separated  with a string of the product_price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class

        GGornalusse,12.5.2021,Modified original code and created version 1

        GGornalusse,12.6.2021,Modified version 1 and created version 2
    """

    # --Fields--
    # strProductName = ""
    # strProductPrice = ""

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Returns Product name with first letter capitalized

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)  # Returns formatted product price as a float

    @product_price.setter
    def product_price(self, value):  # (setter or mutator)
        if value.isisstance(value, float):  # Checks if the value is a float
            self.__product_name = value
        else:
            raise Exception("Product prices cannot be strings or other data types")

    # -- Methods --

    def __str__(self):
        return self.product_name + ',' + str(float(self.product_price))


# --End of class--

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class

        GGornalusse,12.5.2021,Modified original code and created version1

        GGornalusse,12.6.2021,Modified version 1 and created version2
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list of dictionary rows

        :param  file_name: (string) with name of file:

        :param list_of_product_objects: (list) you want filled with file data:

        :return: (list) of dictionary rows
        """
        #list_of_product_objects.clear()  # clear current data
        objfile = open(file_name, "r")
        for line in objfile:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_product_objects.append(row)
        objfile.close()
        return list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data from a list of dictionary rows into a file
        :param file_name: (string) with name of file you want to write using data from the list:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of  rows
        """
        objfile = open(file_name, "w")
        for row in list_of_product_objects:
            objfile.write(row["Product"] + "," + row["Price"] + "\n")
        objfile.close()
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Reload Data from File
            2) Add data to the list of product objects
            3) Save Data to File and Exit Program       
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_product_objects):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products and Prices are: *******")
        for row in list_of_product_objects:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price(product_name, product_price, list_of_product_objects):
        """ Asks for a new product and its corresponding price
        :param product_name  (string) with name of a user's product
        :param product_price: (float) with name of a user's product's price
        :return (string, float) product, price the user entered
        """
        product_name = str(input("Please enter name of the Product: ")).strip()
        product_price = float(input("Please enter its corresponding priority: "))
        print()
        return product_name, product_price


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
list_of_product_objects = FileProcessor.read_data_from_file(file_name, list_of_product_objects)  # read file data


# Show user a menu of options
IO.print_menu_tasks()

# Get user's menu option choice
while True:
    IO.input_menu_choice()

    if choice.strip() == '1':   # Show user current data in the list of product objects
        list_of_product_objects = FileProcessor.read_data_from_file(file_name, list_of_product_objects)
        IO.print_current_products_in_list(list_of_product_objects)
        continue

    elif choice.strip() == '2':  # Let user add data to the list of product objects
        product_name, product_price = IO.input_new_product_and_price(product_name, product_price, list_of_product_objects)
        new_product = Product(product_name, product_price)
        IO.print_current_products_in_list(list_of_product_objects)
        continue

    elif choice.strip () == '3':  # let user save current data to file and exit program
        list_of_product_objects = FileProcessor.save_data_to_file(file_name, list_of_product_objects)
        IO.print_current_products_in_list(list_of_product_objects)
        break

    else:
        print("Please only enter a number between 1 and 3: ")
        continue