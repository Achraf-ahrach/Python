# ----------------------------------------------------
# ----- Object Oriented Programing => Inheritance ----
# ----------------------------------------------------

class Food: # Base class

    def __init__(self, name, price):

        self.name = name
        self.price = price
        print(f"{self.name} Is Created From Base Class")

    def eat(self):

        print("Eat Method From Base Class")


class Apple(Food): # Derived Class

    def __init__(self, name, price, amount):
        
        # Food.__init__(self, name) # Create Instance From Base Class
        
        super().__init__(name, price)

        self.amount = amount

        print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")
    
    def get_from_tree(self):
        print("Get From The From Derived Class")

# food_one = Food("Pizza", 22)
food_two = Apple("Orange", 10, 500)
food_two.eat()
food_two.get_from_tree()
