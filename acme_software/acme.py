import random 

class Product():
    """
    General reperesentation of a product.
    """
    def __init__(self, 
             name = '',
             price = 10,
             weight = 20,
             flammability = 0.5, 
             identifier = random.randint(1000000, 9999999)):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        Calculates the price divided by the weight, and then returns a message: 
        if the ratio is less than 0.5 return "Not so stealable...", 
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.", 
        and otherwise return "Very stealable!"
        """
        ratio = self.price / self.weight
        message1 = '"Not so stealable..."'
        message2 = '"Kinda stealable"'
        message3 = '"Very stealable!"'
        if ratio < 0.5:
            print(message1)
        elif 0.5 <= ratio < 1.0:
            print(message2)
        else:
            print(message3)

    def explode(self):
        """
        Calculates the flammability times the weight, and then returns a message: 
        if the product is less than 10 return "...fizzle.", 
        if it is greater or equal to 10 but less than 50 return "...boom!", 
        and otherwise return "...BABOOM!!"
        """
        likelihood = self.flammability * self.weight
        message1 = '"...fizzle."'
        message2 = '"...boom!"'
        message3 = '"...BABOOM!!"'
        if likelihood < 10:
            print(message1)
        elif 10 <= likelihood < 50:
            print(message2)
        else:
            print(message3)

class BoxingGlove(Product):
    """
    A subclass of product.
    """
    def __init__(self, 
             name = '',
             price = 10,
             weight = 10,
             flammability = 0.5, 
             identifier = random.randint(1000000, 9999999)):
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """
        Calculates the flammability times the weight, and then returns a message: 
        if the product is less than 10 return "...fizzle.", 
        if it is greater or equal to 10 but less than 50 return "...boom!", 
        and otherwise return "...BABOOM!!"
        """
        likelihood = self.flammability * self.weight
        message1 = '"...fizzle."'
        message2 = '"...boom!"'
        message3 = '"...BABOOM!!"'
        print("... it's a glove.")

    def punch(self):
        """
        Returns "That tickles." if the weight is below 5, 
        "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, 
        and "OUCH!" otherwise.
        """
        message1 = '"That tickles."'
        message2 = '"Hey that hurt!"'
        message3 = '"OUCH!"'
        if self.weight < 5:
            print(message1)
        elif 5 <= self.weight < 15:
            print(message2)
        else:
            print(message3) 


    

    









