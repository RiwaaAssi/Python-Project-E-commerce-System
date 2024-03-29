from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, User_id, User_name, User_DoB, Role, Active):
        self.User_id = User_id
        self.User_name = User_name
        self.User_DoB = User_DoB
        self.Role = Role
        self.Active = Active

    def getUser_id(self):
        return self.User_id

    def setUser_id(self, User_id):
        self.User_id = User_id

    def getUser_name(self):
        return self.User_id

    def setUser_name(self, User_name):
        self.User_name = User_name

    def getUser_DoB(self):
        return self.User_id

    def setUser_DoB(self, User_DoB):
        self.User_DoB = User_DoB

    def getRole(self):
        return self.Role

    def setRole(self, Role):
        self.Role = Role

    def getActive(self):
        return self.Active

    def setActive(self, Active):
        self.Active = Active

    def getBasket(self):
        return self.Basket

    def setBasket(self, Basket):
        self.Basket = Basket

    def getOrder(self):
        return self.Order

    def setOrder(self, Order):
        self.Order = Order

    @abstractmethod
    def __str__(self):
        pass


class Admin(User):
    def __init__(self, User_id, User_name, User_DoB, Role, Active):
        super().__init__(User_id, User_name, User_DoB, Role, Active)

    def __str__(self):
        return f"User id: " + str(self.User_id) + "\nUser Name: " + str(
            self.User_name) + "\nDate of Birth: " + str(self.User_DoB) + "\nRole: " + str(
            self.Role) + "\nActive: " + str(self.getActive())


class Shopper(User):
    def __init__(self, User_id, User_name, User_DoB, Role, Active, Basket, Order):
        super().__init__(User_id, User_name, User_DoB, Role, Active)
        self.Basket = Basket
        self.Order = Order

    def __str__(self):
        return f"User id: " + str(self.User_id) + "\nUser Name: " + str(
            self.User_name) + "\nDate of Birth: " + str(self.User_DoB) + "\nRole: " + str(
            self.Role) + "\nActive: " + str(self.Active) + "\nBasket: " + str(
            self.Basket) + "\nOrder: " + str(self.Order)

