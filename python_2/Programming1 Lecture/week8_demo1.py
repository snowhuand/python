class Fruit: #class
    __secret_var ="40" #hidden variable

    def __init__(self, calorie=0, color=""):
        self.calorie = calorie #field/attribute
        self.color = color
        __confidential = "abc"  # private variable meant to be hidden from outsiders, concept of encapsulation
        #print(self.__confidential)

    def __helperMethod(self): #hidden method, similar to hidden variable.
        print("I am hidden.")

    def isHighCalorie(self):
        self.__secret_var
        self.__helperMethod()
        if self.calorie >= 100:
            return True
        return False

    def __mul__(self, other):
        # eg. A * B, you call on __mul__ on A, other will be B
        return "{} multiplied by {} results in {}".format(self.calorie, other.calorie, self.calorie * other.calorie)

    def __str__(self): #method
        return "Fruit class with calorie {} and color {}." \
               "".format(self.calorie, self.color)

class AsiaFruit(Fruit):
    def isHighCalorie(self):
        if self.calorie > 80:
            return True
        return False

class StrawBerry(Fruit): #Strawberry inherits from Fruit class and possess all attributes and methods from superclass
    # StrawBerry - child class/ sub-class
    # Fruit - superclass / parent class
    # Test for inheritance: Strawberry is a Fruit

    def isHighCalorie(self):
        if self.calorie > 50:
            return True
        return False

class Durian(AsiaFruit):
    def isHighCalorie(self): #overloading, over-write the method from parent class
        if self.calorie > 200:
            return True
        return False

    def printOtherProperties(self,  *args): #variable length of arguments passed in as list
        print("In other properties")
        for each in args:# args[0]= spiky, args[1]= smelly
            print("printing contents: {}".format(each))

    def printKeyValueFeatures(self, **kwargs): #key word arguments
        print("in printKeyValueFeatures()")
        for key, value in kwargs.items():
            print("{} -> {}".format(key, value))


durian1 = Durian(200, "Green")
#print(durian1)

papaya = Fruit(200, "Green")
papaya.isHighCalorie()
#print(durian1 * papaya)

#print(durian1 == papaya)
#print(papaya.isHighCalorie())

# durian1.printOtherProperties("spiky", "smelly")
#
# durian1.printKeyValueFeatures(origin="Thailand", years=5) # variable name origin (key), value =Thailand (value)
#
# dict_var = {"key1": 100, "key2": 200}
# durian1.printKeyValueFeatures(**dict_var) # Add ** if using existing dictionary
# fruitA = Fruit(100, "yellow") #object
# print(fruitA)
# print(fruitA.isHighCalorie())
# #print(fruitA.calorie)
# #print(Fruit.__confidential)
# strawberry1 = StrawBerry(60, "red")
# print(strawberry1.isHighCalorie()) # specificity rule, the nearest method will be used, else traverse to higher
# #hierachy until the method is found
#
# durian1 = Durian(150, "Green")
# print(durian1.isHighCalorie())
#
# print(AsiaFruit(1000, "Green"))
"""
Fruit
  ^
  |
AsiaFruit
  ^
  |
Durian

"""