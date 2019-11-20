"""
This module is an implementation of movie ticket system.
It collects the quantiy of movie tickets needed.....

Author: Yok Yen
Date: 7 Sept 2016
Version: 1.0
"""

ADULT_TICKET_PRICE = 10
CHILD_TICKET_PRICE = 5
CONC_TICKET_PRICE = 8
PREMIUM_FACTOR = 2
EXTRAVAGANT_FACTOR = 5
LUCKYNUM = 2

def getQuantity(prompt):
    """ This function gets the quantity base on the prompt.
    function getQuantity( prompt):
        display prompt
        get value from user
        while value is less than zero:
        print an error
        display prompt
        get value
        return ‘value’
    :param prompt: The message to display to user
    :return: The quantity user entered.
    """
    value = int(input(prompt + "\n>>>"))
    while value < 0:   #While loop to display error message when the quantity is below 0
        print("Error in input.")
        value = int(input(prompt + "\n>>>"))
    return value

def calcTotalCost(packageCode, numAdultTickets, numChildTickets, numConcTickets):
    adultCost = numAdultTickets * ADULT_TICKET_PRICE
    childCost = numChildTickets * CHILD_TICKET_PRICE
    concCost = numConcTickets * CONC_TICKET_PRICE
    totalCost = adultCost + childCost + concCost
    if packageCode == 'P':
	    totalCost = totalCost * PREMIUM_FACTOR
    elif packageCode == 'E':
        totalCost = totalCost * EXTRAVAGANT_FACTOR
    return totalCost

def getDiscount():
    import random
    rand_num = random.randint(1, 10)

    if rand_num == LUCKYNUM:
        discount = True
    else:
        discount = False
    return discount

def main():
    package = input("Welcome \n Enter your choice(B, P, E):").upper()

    while package not in ['B', 'P', 'E']:
        print("Error")
        package = input("Welcome \n Enter your choice(B, P, E):").upper()

    adultTickets = getQuantity("How many adult tickets? ")
    childTickets = getQuantity("How many child tickets? ")
    concTickets = getQuantity("How many concession tickets? ")
    ticketCost = calcTotalCost(package, adultTickets, childTickets, concTickets)
    print("test:", ticketCost)
    discounted = False
    if ticketCost > 100:
        discounted = getDiscount()
    if discounted == True :
        ticketCost = ticketCost * 0.8
        print("You received a 20% discount")
    print("Final cost: ", ticketCost)
main()