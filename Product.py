from enum import Enum

class Category(Enum):

    def __init__(self, name):
        self.name = name


class Product:
    def __init__(self, Product_id, Product_name, Product_category, Price, Inventory, Supplier, Has_an_offer,
                 Offer_price,
                 Valid_until):
        self.Product_id = Product_id
        self.Product_name = Product_name
        self.Product_category = Product_category
        self.Price = Price
        self.Inventory = Inventory
        self.Supplier = Supplier
        self.Has_an_offer = Has_an_offer
        self.Offer_price = Offer_price
        self.Valid_until = Valid_until

    def getProduct_id(self):
        return self.Product_id

    def setProduct_id(self, Product_id):
        self.Product_id = Product_id

    def getProduct_name(self):
        return self.Product_name

    def setProduct_name(self, Product_name):
        self.Product_name = Product_name

    def getProduct_category(self):
        return self.Product_category

    def setProduct_category(self, Product_category):
        self.Product_category = Product_category

    def getPrice(self):
        return self.Price

    def setPrice(self, Price):
        self.Price = Price

    def getInventory(self):
        return self.Inventory

    def setInventory(self, Inventory):
        self.Inventory = Inventory

    def getSupplier(self):
        return self.Supplier

    def setSupplier(self, Supplier):
        self.Supplier = Supplier

    def getHas_an_offer(self):
        return self.Has_an_offer

    def setHas_an_offer(self, Has_an_offer):
        self.Has_an_offer = Has_an_offer

    def getOffer_price(self):
        return self.Offer_price

    def setOffer_price(self, Offer_price):
        self.Offer_price = Offer_price

    def getValid_until(self):
        return self.Valid_until

    def setValid_until(self, Valid_until):
        self.Valid_until = Valid_until

    def __str__(self):
        return f"Product id: " + str(self.Product_id) + "\nProduct Name: " + str(
            self.Product_name) + "\nProduct Category: " + str(self.Product_category) + "\nPrice: " + str(
            self.Price) + "\nInventory: " + str(self.Inventory) + "\nSupplier: " + str(
            self.Supplier) + "\nHas An Offer: " + str(self.Has_an_offer) + "\nOffer Price:" + str(
            self.Offer_price) + "\nValid Until:" + str(self.Valid_until)

