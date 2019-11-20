"""
Creating your own exception
"""
class LowInventoryException(Exception):
    def __init__(self):
        print("Low inventory alert!!!!")

"""
Using the exception you have created
"""
def test():
    inventory = 11
    if inventory < 10:
        raise LowInventoryException

"""
Managing exception
"""
try:
    test()
except LowInventoryException:
    print("You have to replenish stocks!!")
else:
    print("No exception occurs")
finally:
    print("Everyone gets to this")