from datetime import datetime
from User import *
from Product import *


################################################## Needed Functions ####################################################

# Function to parse the dictionary string and convert it to a Python dictionary
def parse_dictionary(dictionary_str):
    try:
        # Removing the curly braces and splitting by ',' to get key-value pairs
        key_value_pairs = dictionary_str.strip('{}').split(',')
        # Splitting each key-value pair by ':' and creating a dictionary
        dictionary = {int(pair.split(':')[0]): int(pair.split(':')[1]) for pair in key_value_pairs}
        return dictionary
    except ValueError:
        # Handle any conversion errors here
        return {}


def printProductList():
    for Product in product_list:
        print(Product)
        print("\n")


def printUserList():
    for user in user_list:
        print(user)
        print("\n")


def find_ID(id, user_list):
    for i in range(len(user_list)):
        if (int(user_list[i].getUser_id()) == int(id)):
            role = user_list[i].getRole()
            return [True, role]
        else:
            continue
    return [False, ""]


def find_ProductID(id, product_list):
    for i in range(len(product_list)):
        if (int(product_list[i].getProduct_id()) == int(id)):
            return True
        else:
            continue
    return False


def findandSet(product_list, id, offer_price, formatted_date):
    for i in range(len(product_list)):
        if (int(product_list[i].getProduct_id()) == int(id)):
            product_list[i].setHas_an_offer(1)
            product_list[i].setOffer_price(offer_price)
            product_list[i].setValid_until(formatted_date)


def setProduct(product_list, id, name, category, price, inv, sup, offer, offer_price, formatted_date):
    for i in range(len(product_list)):
        if (int(product_list[i].getProduct_id()) == int(id)):
            product_list[i].setProduct_name(name)
            product_list[i].setProduct_category(category)
            product_list[i].setOffer_price(offer_price)
            product_list[i].setSupplier(sup)
            product_list[i].setHas_an_offer(offer)
            product_list[i].setInventory(inv)
            product_list[i].setPrice(price)
            product_list[i].setValid_until(formatted_date)


def printShopper(User_ID):
    for user in shopper_list:
        if (int(user.getUser_id()) == int(User_ID)):
            print(user)


def setUser(user_list, id, name, formatted_date, role, active, basket, order):
    for user in user_list:
        if (int(user.getUser_id()) == int(id)):
            user.setUser_DoB(formatted_date)
            user.setUser_name(name)
            user.setRole(role)
            user.setActive(active)

            if (str(user.getRole()).lower() == "admin"):
                for j in range(len(admin_list)):
                    if (int(admin_list[j].getUser_id()) == int(id)):
                        admin_list[j].setUser_DoB(formatted_date)
                        admin_list[j].setUser_name(name)
                        admin_list[j].setRole(role)
                        admin_list[j].setActive(active)

                        break


            elif (str(user.getRole()).lower() == "shopper"):

                for j in range(len(shopper_list)):
                    if (int(shopper_list[j].getUser_id()) == int(id)):
                        shopper_list[j].setUser_DoB(formatted_date)
                        shopper_list[j].setUser_name(name)
                        shopper_list[j].setRole(role)
                        shopper_list[j].setActive(active)
                        shopper_list[j].setBasket(basket)
                        shopper_list[j].setOrder(order)
                        user.setBasket(basket)
                        user.setOrder(order)
                        break


def printoffers(product_list):
    for i in range(len(product_list)):
        if (int(product_list[i].getHas_an_offer()) == 1):
            print(product_list[i])
            print("\n")


def printCategory(product_list, cat):
    for i in range(len(product_list)):
        if (str(product_list[i].getProduct_category()).lower() == str(cat).lower()):
            print(product_list[i])
            print("\n")


def printProductName(product_list, name):
    for i in range(len(product_list)):
        if (str(product_list[i].getProduct_name()).lower() == str(name).lower()):
            print(product_list[i])
            print("\n")


def printShopperList():
    for shopper in shopper_list:
        print(shopper)
        print("\n")


def purchaseBasket():
    for i in range(len(shopper_list)):
        if (not (len(shopper_list[i].getBasket()) == 0)):
            all_values_zero = all(value == 0 for value in dict(shopper_list[i].getBasket()).values())
            if not all_values_zero:
                print(shopper_list[i])
                print("\n")


def printUnunprocessedOrder(shopper_list):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getOrder()) == 0):
            if (not (len(shopper_list[i].getBasket()) == 0)):
                all_values_zero = all(value == 0 for value in dict(shopper_list[i].getBasket()).values())
                if not all_values_zero:
                    print(shopper_list[i])
                    print("\n")


def chekBasket(UserID, shopper_list):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(UserID)):
            if (len(shopper_list[i].getBasket()) == 0):
                return False
            else:
                return True


def findProductInBasket(product_id, UserID, shopper_list):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(UserID)):
            if (not (len(dict(shopper_list[i].getBasket())) == 0)):
                for key in dict(shopper_list[i].getBasket()).keys():
                    if (int(key) == int(product_id)):
                        return True
                return False


def getBasket(User_ID):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):
            return shopper_list[i].getBasket()


def printBasket(User_ID, shopper_list):
    total_cost = 0
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):

            for key in dict(shopper_list[i].getBasket()).keys():
                for j in range(len(product_list)):
                    if (int(product_list[j].getProduct_id()) == int(key)):
                        product = product_list[j]
                        print(product_list[j])
                        if (int(product.getHas_an_offer()) == 1):
                            cost = int(product.getOffer_price()) * int(dict(shopper_list[i].getBasket())[key])
                            total_cost = int(total_cost) + int(cost)
                            print("Number of items: " + str(dict(shopper_list[i].getBasket())[key]))
                            print("Cost of the purchase in the product: " + str(cost))

                        else:
                            cost = int(product.getPrice()) * int(dict(shopper_list[i].getBasket())[key])
                            print("Number of items: " + str(dict(shopper_list[i].getBasket())[key]))
                            print("Cost of the purchase in the product: " + str(cost))
                            total_cost = int(total_cost) + int(cost)
                            print("\n")
    print("--------------------------")
    print("Basket Cost=" + str(total_cost))


def clearBasket(User_ID):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):
            shopper_list[i].setBasket(dict({}))

    for j in range(len(user_list)):
        if (int(user_list[j].getUser_id()) == int(User_ID)):
            user_list[j].setBasket(dict({}))


def deleteProductfromBasket(product_id, User_ID, shopper_list, user_list):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):
            basket = shopper_list[i].getBasket()
            basket = dict(basket)
            for key in dict(shopper_list[i].getBasket()).keys():
                if (int(key) == int(product_id)):
                    basket.pop(int(product_id))
                    shopper_list[i].setBasket(dict(basket))

    for j in range(len(user_list)):
        if (int(user_list[j].getUser_id()) == int(User_ID)):
            basket = user_list[j].getBasket()
            basket = dict(basket)
            for key in dict(user_list[j].getBasket()).keys():
                if (int(key) == int(product_id)):
                    basket.pop(int(product_id))
                    user_list[j].setBasket(dict(basket))


def findandSetBasket(product_id, User_ID, shopper_list, user_list, num):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):
            if (not (len(dict(shopper_list[i].getBasket())) == 0)):
                for key in dict(shopper_list[i].getBasket()).keys():
                    if (int(key) == int(product_id)):
                        basket = dict(shopper_list[i].getBasket())
                        basket[key] = int(num)
                        shopper_list[i].setBasket(dict(basket))

    for i in range(len(user_list)):
        if (int(user_list[i].getUser_id()) == int(User_ID)):
            if (not (len(dict(user_list[i].getBasket())) == 0)):
                for key in dict(user_list[i].getBasket()).keys():
                    if (int(key) == int(product_id)):
                        basket = dict(user_list[i].getBasket())
                        basket[key] = int(num)
                        user_list[i].setBasket(dict(basket))


def setOrder(User_ID, shopper_list, user_list):
    for i in range(len(shopper_list)):
        if (int(shopper_list[i].getUser_id()) == int(User_ID)):
            if (not (len(dict(shopper_list[i].getBasket())) == 0)):
                all_values_zero = all(value == 0 for value in dict(shopper_list[i].getBasket()).values())
                if not all_values_zero:
                    shopper_list[i].setOrder(1)

    for i in range(len(user_list)):
        if (int(user_list[i].getUser_id()) == int(User_ID)):
            if (not (len(dict(user_list[i].getBasket())) == 0)):
                all_values_zero = all(value == 0 for value in dict(user_list[i].getBasket()).values())
                if not all_values_zero:
                    user_list[i].setOrder(1)


def Execute_order(shopper_list, user_list, product_list):
    for shopper in shopper_list:
        order = int(shopper.getOrder())
        basket_dict = shopper.getBasket()

        if order == 1 and basket_dict:
            for product in product_list:
                product_id = int(product.getProduct_id())

                if product_id in basket_dict:
                    basket_quantity = int(basket_dict[product_id])
                    inventory = product.getInventory()

                    if basket_quantity <= inventory:
                        product.setInventory(inventory - basket_quantity)

            # Clear the basket and set order to 0
            shopper.setBasket({})
            shopper.setOrder(0)

    for shopper in user_list:
        if (str(shopper.getRole()).lower() == "shopper"):
            order = int(shopper.getOrder())
            basket_dict = shopper.getBasket()

            if order == 1 and basket_dict:
                for product in product_list:
                    product_id = int(product.getProduct_id())

                    if product_id in basket_dict:
                        basket_quantity = int(basket_dict[product_id])
                        inventory = product.getInventory()

                        if basket_quantity <= inventory:
                            product.setInventory(inventory - basket_quantity)

                # Clear the basket and set order to 0
                shopper.setBasket({})
                shopper.setOrder(0)

    # for i in range(len(shopper_list)):
    #     if (int(shopper_list[i].getOrder()) == 1):
    #         if ((not (len(dict(shopper_list[i].getBasket())) == 0))):
    #             for k in range(len(product_list)):
    #                 for key in dict(shopper_list[i].getBasket()).keys():
    #                     if (int(product_list[k].getProduct_id()) == int(key)):
    #                         if (dict(shopper_list[i].getBasket())[key] <= product_list[k].getInventory()):
    #                             product_list[k].setInventory(
    #                                     int(product_list[k].getInventory()) - int(dict(shopper_list[i].getBasket())[key]))
    #                             basket = {}
    #                             shopper_list[i].setBasket(basket)
    #                             shopper_list[i].setOrder(0)

    # for i in range(len(user_list)):
    #     if (str(user_list[i].getRole()).lower() == "shopper"):
    #         if (int(user_list[i].getOrder()) == 1):
    #             if ((not (len(dict(user_list[i].getBasket())) == 0)) and (int(user_list[i].getOrder()) == 1)):
    #                 for key in dict(user_list[i].getBasket()).keys():
    #                     for k in range(len(product_list)):
    #                         if (product_list[k].getProduct_id() == key):
    #                             if (int(user_list[i].getBasket()[key]) <= int(product_list[k].getInventory())):
    #                                 user_list[i].setOrder(0)
    #                                 basket = {}
    #                                 user_list[i].setBasket(basket)


################################################## Reading Product File ###############################################
with open('Products.txt') as f:
    product_list = []
    formatted_date = ""
    for line in f:
        try:
            fields = line.strip().split(';')
            date_parts = fields[-1].split('/')
            day = int(date_parts[0])
            month = int(date_parts[1])
            year = int(date_parts[2])

            date_object = datetime(year, month, day)
            formatted_date = date_object.strftime("%d/%m/%Y")

        except ValueError:
            formatted_date = "0/0/0"

        try:
            if (not (str(fields[0]).isdigit() and len(str(fields[0])) == 6)):
                continue

            if (find_ProductID(int(fields[0]), product_list)):
                continue

            product = Product(int(fields[0]), str(fields[1]), str(fields[2]), int(fields[3]), int(fields[4]),
                              str(fields[5]),
                              int(fields[6]), int(fields[7]), formatted_date)
            product_list.append(product)

        except (ValueError):
            print("Product Invalid Input")
            continue

f.close()

################################################## Reading Users File ##################################################
# Open the file for reading
with open('Users.txt', 'r') as file:
    lines = file.readlines()

user_list = []
shopper_list = []
admin_list = []

# Iterate through each line in the file
for line in lines:

    # Split the line by ';'
    fields = line.strip().split(';')
    formatted_date = ""

    try:
        # Parse the date (assuming it's in the format "day/month/year")
        date_parts = fields[2].split('/')
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])

        date_object = datetime(year, month, day)
        formatted_date = date_object.strftime("%d/%m/%Y")

    except ValueError:
        formatted_date = "0/0/0"

    try:

        if (not (str(fields[0]).isdigit() and len(str(fields[0])) == 6)):
            continue

        if (find_ID(fields[0], user_list)[0]):
            continue

        # Create a User object and append it to the user_list
        if (str(fields[3]).lower() == "admin"):
            user = Admin(fields[0], fields[1], formatted_date, fields[3], int(fields[4]))
            admin_list.append(user)
        else:
            # Parse the dictionary from the field
            dictionary_str = fields[5]

            # Create a dictionary from the string
            dictionary = parse_dictionary(dictionary_str)

            user = Shopper(fields[0], fields[1], formatted_date, fields[3], int(fields[4]), dictionary, int(fields[6]))
            shopper_list.append(user)

        user_list.append(user)

    except (ValueError):
        print("User Invalid Input")
        continue

file.close()
############################################### Program Menu ##########################################################
print("Welcome to Our E-commerce System")
while (True):
    try:
        ProductHaveSaved = False
        UserHaveSaved = False

        User_ID = input("What is your ID? ")
        User_ID = int(User_ID)

        if (not (str(User_ID).isdigit() and len(str(User_ID)) == 6)):
            print("Please enter a number contains 6 digit ")
            continue

        if (not find_ID(User_ID, user_list)[0]):
            print("This user does not exist, Please try again\n ")
            continue


    except (ValueError):
        print("Please Enter an integer number")
        continue

    flag = find_ID(User_ID, user_list)
    Role = flag[1]
    break

while (True):
    print("=========================================================================================")
    print("Choose one option form below")
    choose = input(
        "1. Add product (admin-only)\n2. Place an item on sale (admin-only)\n3. Update product (admin-only)\n4. Add a new user (admin-only)\n" +
        "5. Update user (admin-only)\n6. Display all users (admin-only)\n7. List products (admin and shopper)\n8. List shoppers (admin)\n" +
        "9. Add product to the basket (shopper-only)\n10. Display basket (shopper-only)\n11. Update basket (shopper-only)\n12. Place order (shopper-only)\n" +
        "13. Execute order (admin-only)\n14. Save products to a file (admin-only)\n15. Save users to a text file (admin-only)\n16. Exit\n")
    choose = int(choose)


    if (int(choose) == 1):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Add product")
                    id = input("Product ID (6 digit only): ")
                    if (not (str(id).isdigit() and len(str(id)) == 6)):
                        print("Please enter a number contains 6 digit ")
                        continue
                    if (find_ProductID(id, product_list)):
                        print("This Product exists, Please try Again\n")
                        continue
                    name = input("Product Name: ")
                    name = str(name)
                    cat = input("Product Category: ")
                    category = str(cat)
                    price = input("Product Price: ")
                    price = int(price)
                    inv = input("Product Inventory: ")
                    inv = int(inv)
                    sup = input("Product Supplier: ")
                    sup = str(sup)
                    offer = input("Product Has_on_offer: ")
                    offer = int(offer)
                    product = Product(id, name, category, price, inv, sup, offer, 0, "")
                    product_list.append(product)

                    break


                except (ValueError):
                    print("Invalid Input, Please try again")
                    continue



        else:
            print("Access Denied\n")
            continue



    elif (int(choose) == 2):

        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Place an item on sale")
                    id = input("Product ID (6 digit only): ")

                    if (not (str(id).isdigit() and len(str(id)) == 6)):
                        print("Please enter a number contains 6 digit ")
                        continue

                    if (not find_ProductID(id, product_list)):
                        print("This product does not exist, Please try again\n ")
                        continue

                    offer_price = input("Product offer Price: ")
                    offer_price = int(offer_price)
                    date_str = input("Please enter a date (DD/MM/YYYY): ")

                    date_parts = date_str.split('/')
                    day = int(date_parts[0])
                    month = int(date_parts[1])
                    year = int(date_parts[2])

                    date_object = datetime(year, month, day)
                    formatted_date = date_object.strftime("%d/%m/%Y")
                    findandSet(product_list, id, offer_price, formatted_date)
                    break

                except (ValueError):
                    print("Please try again")
                    continue

        else:
            print("Access Denied")
            continue




    elif (int(choose) == 3):

        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Update product")

                    id = input("Product ID (6 digit only): ")

                    if (not (str(id).isdigit() and len(str(id)) == 6)):
                        print("Please enter a number contains 6 digit ")
                        continue

                    if (not find_ProductID(id, product_list)):
                        print("This product does not exist, Please try again\n ")
                        continue

                    name = input("Product Name: ")
                    name = str(name)
                    cat = input("Product Category: ")
                    category = str(cat)
                    price = input("Product Price: ")
                    price = int(price)
                    inv = input("Product Inventory: ")
                    inv = int(inv)
                    sup = input("Product Supplier: ")
                    sup = str(sup)
                    offer = input("Product Has_on_offer: ")
                    offer = int(offer)

                    if (int(offer) == 1):
                        offer_price = input("Product offer Price: ")
                        offer_price = int(offer_price)
                        date_str = input("Please enter a date (DD/MM/YYYY): ")

                        date_parts = date_str.split('/')
                        day = int(date_parts[0])
                        month = int(date_parts[1])
                        year = int(date_parts[2])

                        date_object = datetime(year, month, day)
                        formatted_date = date_object.strftime("%d/%m/%Y")
                    else:
                        offer_price = 0
                        formatted_date = "0/0/0"

                    setProduct(product_list, id, name, category, price, inv, sup, offer, offer_price, formatted_date)
                    break

                except (ValueError):
                    print("Please try again")
                    continue

        else:
            print("Access Denied")
            continue



    elif (int(choose) == 4):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Add a new user")

                    id = input("User ID (6 digit only): ")

                    if (not (str(id).isdigit() and len(str(id)) == 6)):
                        print("Please enter a number contains 6 digit ")
                        continue

                    if (find_ID(id, user_list)[0]):
                        print("This user exists, Please try again\n ")
                        continue

                    name = input("User Name: ")
                    name = str(name)

                    date_str = input("Please User Date of Birth (DD/MM/YYYY): ")

                    date_parts = date_str.split('/')
                    day = int(date_parts[0])
                    month = int(date_parts[1])
                    year = int(date_parts[2])

                    date_object = datetime(year, month, day)
                    formatted_date = date_object.strftime("%d/%m/%Y")

                    role = input("User Role: ")
                    role = str(role)
                    active = input("User Active: ")
                    active = int(active)

                    # print("User Basket:\n")
                    # basket = {}
                    # loops=input("How many products do you need? ")
                    # for i in range(int(loops)):
                    #     product_id=input("Product ID (6 digit only): ")
                    #     if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                    #         print("Please enter a number contains 6 digit ")
                    #         continue
                    #     if (not find_ProductID(product_id, product_list)):
                    #         print("This product does not exist, Please try again\n ")
                    #         continue
                    # for i in basket.keys():
                    #     if (int(basket[i]) == 0):
                    #         continue
                    #     else:
                    #         break
                    #     basket={}
                    #
                    #     basket[int(product_id)]=int(input("Number of items: "))
                    #
                    # order = input("User Order: ")
                    # order = int(order)

                    if (str(role).lower() == "admin"):
                        user = Admin(id, name, formatted_date, role, active)
                        admin_list.append(user)

                    else:
                        user = Shopper(id, name, formatted_date, role, active, {}, 0)
                        shopper_list.append(user)

                    user_list.append(user)
                    break

                except (ValueError):
                    print("Please try again")
                    continue


        else:
            print("Access Denied")
            continue

    elif (int(choose) == 5):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Update user")

                    id = input("User ID (6 digit only): ")

                    if (not (str(id).isdigit() and len(str(id)) == 6)):
                        print("Please enter a number contains 6 digit ")
                        continue

                    if (not find_ID(id, user_list)[0]):
                        print("This user does not exist, Please try again\n ")
                        continue

                    name = input("User Name: ")
                    name = str(name)

                    date_str = input("Please User Date of Birth (DD/MM/YYYY): ")

                    date_parts = date_str.split('/')
                    day = int(date_parts[0])
                    month = int(date_parts[1])
                    year = int(date_parts[2])

                    date_object = datetime(year, month, day)
                    formatted_date = date_object.strftime("%d/%m/%Y")

                    role = input("User Role: ")
                    role = str(role)
                    active = input("User Active: ")
                    active = int(active)

                    if (str(role).lower() == "shopper"):

                        basket = {}

                        print("User Basket:")
                        loops = input("How many products do you want? ")
                        for i in range(int(loops)):
                            product_id = input("Product ID (6 digit only): ")
                            if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                                print("Please enter a number contains 6 digit ")
                                continue

                            if (not find_ProductID(product_id, product_list)):
                                print("This product does not exist, Please try again\n ")
                                continue

                            basket[int(product_id)] = int(input("Number of items: "))

                        all_values_zero = all(value == 0 for value in basket.values())

                        if not all_values_zero:
                            basket = {}

                        order = input("User Order: ")
                        order = int(order)

                        setUser(user_list, id, name, formatted_date, role, active, basket, order)

                    else:
                        setUser(user_list, id, name, formatted_date, role, active, {}, 0)

                    # printUserList()
                    break

                except (ValueError):
                    print("Please try again")
                    continue


        else:
            print("Access Denied")
            continue

    elif (int(choose) == 6):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Display all users\n")
                    printUserList()
                    break

                except (ValueError):
                    print("Please try again")
                    continue


        else:
            print("Access Denied")
            continue

    elif (int(choose) == 7):
        while (True):
            try:
                print("------------------------------------------------------------------------")
                print("List products (choose one from the option):")
                ch = input(
                    "1.All products\n2.Products that have offers/discount\n3.Products belonging to a specific category\n4.Product Name\n")
                if (int(ch) == 1):
                    printProductList()
                    break

                elif (int(ch) == 2):
                    printoffers(product_list)
                    break

                elif (int(ch) == 3):
                    cat = input("Enter Category Name: ")
                    cat = str(cat)
                    printCategory(product_list, cat)
                    break

                elif (int(ch) == 4):
                    name = input("Enter Product Name: ")
                    name = str(name)
                    printProductName(product_list, name)
                    break

                else:
                    print("Please choose one from the option")
                    continue

            except (ValueError):
                print("Please try again")
                continue



    elif (int(choose) == 8):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("List shoppers\nchoose one from the option:")
                    ch = input(
                        "1.All shoppers\n2.All shoppers that have added products for purchase to the basket.\n3.Shoppers that has unprocessed orders\n")

                    if (int(ch) == 1):
                        printShopperList()
                        break

                    elif (int(ch) == 2):
                        purchaseBasket()
                        break

                    elif (int(ch) == 3):
                        printUnunprocessedOrder(shopper_list)
                        break
                    else:
                        print("Please choose one from the option")
                        continue


                except (ValueError):
                    print("Please try again")
                    continue
        else:
            print("Access Denied")
            continue
    elif (int(choose) == 9):
        if (str(Role).lower() == "shopper"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    flag = chekBasket(User_ID, shopper_list)
                    if not flag:
                        basket = {}
                        loops = input("How many products do you need? ")

                        for i in range(int(loops)):
                            product_id = input("Product ID (6 digit only): ")
                            if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                                print("Please enter a number contains 6 digit ")
                                continue

                            if (not find_ProductID(product_id, product_list)):
                                print("This product does not exist, Please try again\n ")
                                continue

                            basket[int(product_id)] = int(input("Number of items: "))

                        all_values_zero = all(value == 0 for value in basket.values())

                        if not all_values_zero:
                            basket = {}
                    else:
                        basket = getBasket(User_ID)
                        loops = input("How many products do you need? ")
                        for i in range(int(loops)):
                            product_id = input("Product ID (6 digit only): ")
                            if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                                print("Please enter a number contains 6 digit ")
                                continue

                            if (not find_ProductID(product_id, product_list)):
                                print("This product does not exist, Please try again\n ")
                                continue

                            if (findProductInBasket(product_id, User_ID, shopper_list)):
                                check = input(
                                    "This product already exists in your basket, do you want to reset the value of it? (yes / no)\n ")
                                if (str(check).lower() == "no"):
                                    continue

                            basket[int(product_id)] = int(input("Number of items: "))

                        all_values_zero = all(value == 0 for value in basket.values())

                        if not all_values_zero:
                            basket = {}

                    printShopper(User_ID)

                    break

                except (ValueError):
                    print("Please try again")
                    continue

        else:
            print("Access Denied")
            continue
    elif (int(choose) == 10):
        if (str(Role).lower() == "shopper"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print(f"Display basket for user: {User_ID}")
                    printBasket(User_ID, shopper_list)
                    break

                except (ValueError):
                    print("Please try again")
                    continue


        else:
            print("Access Denied")
            continue
    elif (int(choose) == 11):
        if (str(Role).lower() == "shopper"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Update basket (choose one from the option)")
                    ch = input(
                        "1.Remove all products from the basket\n2.Remove a specific product from the basket based on product id.\n3.Change the number of items of a particular product in the basket based on product id\n")

                    if (int(ch) == 1):
                        clearBasket(User_ID)
                        printShopper(User_ID)

                        break

                    elif (int(ch) == 2):
                        product_id = input("Product ID (6 digit only): ")
                        if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                            print("Please enter a number contains 6 digit ")
                            continue

                        if (not find_ProductID(product_id, product_list)):
                            print("This product does not exist, Please try again\n ")
                            continue

                        deleteProductfromBasket(product_id, User_ID, shopper_list, user_list)

                        printShopper(User_ID)

                        break

                    elif (int(ch) == 3):

                        product_id = input("Product ID (6 digit only): ")
                        if (not (str(product_id).isdigit() and len(str(product_id)) == 6)):
                            print("Please enter a number contains 6 digit ")
                            continue

                        if (not find_ProductID(product_id, product_list)):
                            print("This product does not exist, Please try again\n ")
                            continue
                        num = input("Number of Items: ")
                        findandSetBasket(product_id, User_ID, shopper_list, user_list, int(num))

                        printShopper(User_ID)

                        break
                    else:
                        print("Please choose one from the option")
                        continue

                except (ValueError):
                    print("Please try again")
                    continue

        else:
            print("Access Denied")
            continue
    elif (int(choose) == 12):
        if (str(Role).lower() == "shopper"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Place order")
                    setOrder(User_ID, shopper_list, user_list)
                    printShopper(User_ID)

                    break


                except (ValueError):
                    print("Please try again")
                    continue

        else:
            print("Access Denied")
            continue

    elif (int(choose) == 13):
        if (str(Role).lower() == "admin"):
            while (True):
                try:
                    print("------------------------------------------------------------------------")
                    print("Execute order")
                    Execute_order(shopper_list, user_list, product_list)
                    print("************************** Shopper List ******************************")
                    printShopperList()
                    print("************************** Product List ******************************")
                    printProductList()
                    break

                except (ValueError):
                    print("Please try again")
                    continue
        else:
            print("Access Denied")
            continue
    elif (int(choose) == 14):
        if (str(Role).lower() == "admin"):
            while (True):
                print("------------------------------------------------------------------------")
                print("Save products to a file")
                ProductHaveSaved = True
                # Step 1: Prompt the Admin for the File Name
                file_name = input("Enter the name of the text file to save product data: ")

                # Step 2: Open the File for Writing
                try:
                    with open(file_name, 'w') as file:
                        # Step 3: Write Product Data to the File
                        for product in product_list:
                            product_data = f"Product ID: {product.getProduct_id()}\n"
                            product_data += f"Name: {product.getProduct_name()}\n"
                            product_data += f"Category: {product.getProduct_category()}\n"
                            product_data += f"Price: {product.getPrice()}\n"
                            product_data += f"Inventory: {product.getInventory()}\n"
                            product_data += f"Supplier: {product.getSupplier()}\n"
                            product_data += f"Has an offer: {product.getHas_an_offer()}\n"
                            product_data += f"Offer Price: {product.getOffer_price()}\n"
                            product_data += f"Valid Until: {product.getValid_until()}\n\n"
                            file.write(product_data)
                    print(f"Product data has been saved to {file_name}")

                except FileNotFoundError:
                    print(f"Error: The file '{file_name}' could not be found.")
                except Exception as e:
                    print(f"An error occurred while saving the data: {e}")

                # Step 4: File is automatically closed when exiting the 'with' block
                file.close()

                with open("Saved_Products.txt", 'w') as file:
                    # Step 3: Write Product Data to the File
                    for product in product_list:
                        product_data = f"{product.getProduct_id()};"
                        product_data += f"{product.getProduct_name()};"
                        product_data += f"{product.getProduct_category()};"
                        product_data += f"{product.getPrice()};"
                        product_data += f"{product.getInventory()};"
                        product_data += f"{product.getSupplier()};"
                        product_data += f"{product.getHas_an_offer()};"
                        product_data += f"{product.getOffer_price()};"
                        product_data += f"{product.getValid_until()}\n"
                        file.write(product_data)
                file.close()

                break


        else:
            print("Access Denied")
            continue
    elif (int(choose) == 15):
        if (str(Role).lower() == "admin"):
            while (True):
                print("------------------------------------------------------------------------")
                print("Save users to a text file")
                UserHaveSaved = True
                # Step 1: Prompt the Admin for the File Name
                file_name = input("Enter the name of the text file to save user data: ")

                # Step 2: Open the File for Writing
                try:
                    with open(file_name, 'w') as file:
                        # Step 3: Write Product Data to the File
                        for user in user_list:
                            user_data = f"User ID: {user.getUser_id()}\n"
                            user_data += f"Name: {user.getUser_name()}\n"
                            user_data += f"Date of Birth: {user.getUser_DoB()}\n"
                            user_data += f"Role: {user.getRole()}\n"

                            if (str(user.getRole()).lower() == "shopper"):
                                user_data += f"Active: {user.getActive()}\n"
                                user_data += f"Active: {user.getBasket()}\n"
                                user_data += f"Basket: {user.getOrder()}\n\n"

                            elif (str(user.getRole()).lower() == "admin"):
                                user_data += f"Active: {user.getActive()}\n\n"

                            file.write(user_data)

                    print(f"User data has been saved to {file_name}")

                except FileNotFoundError:
                    print(f"Error: The file '{file_name}' could not be found.")
                except Exception as e:
                    print(f"An error occurred while saving the data: {e}")

                # Step 4: File is automatically closed when exiting the 'with' block
                file.close()

                with open("Saved_Users.txt", 'w') as file:
                    # Step 3: Write Product Data to the File
                    for user in user_list:
                        user_data = f"{user.getUser_id()};"
                        user_data += f"{user.getUser_name()};"
                        user_data += f"{user.getUser_DoB()};"
                        user_data += f"{user.getRole()};"

                        if (str(user.getRole()).lower() == "shopper"):
                            user_data += f"{user.getActive()};"
                            user_data += f"{user.getBasket()};"
                            user_data += f"{user.getOrder()}\n"

                        elif (str(user.getRole()).lower() == "admin"):
                            user_data += f"{user.getActive()}\n"
                        file.write(user_data)
                file.close()

                break

        else:
            print("Access Denied")
            continue
    elif (int(choose) == 16):
        if (UserHaveSaved and ProductHaveSaved):
            break

        if (ProductHaveSaved and not UserHaveSaved):
            flag = input("You have not saved the User file, are you sure you want to exit? (yes or no) ")
            if (str(flag) == "yes"):
                break
            else:
                continue

        if (UserHaveSaved and not ProductHaveSaved):
            flag = input("You have not saved the Product file, are you sure you want to exit? (yes or no) ")
            if (str(flag) == "yes"):
                break
            else:
                continue
        if (not UserHaveSaved and not ProductHaveSaved):
            flag = input("You have not saved any file, are you sure you want to exit? (yes or no) ")
            if (str(flag) == "yes"):
                break
            else:
                continue
        break
    else:
        print("Please choose one from the option")
        continue
