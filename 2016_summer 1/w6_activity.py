
def getQuantity(prompt):
    value = int(input(prompt))
    while value <= 0:
        print("Error!")
        print(prompt)
        value = int(input(prompt))
    return value

def calcTotalCost(packageCode, numAdultTickets, numChildTickets, numConcTickets):
    ADULT_TICKET_PRICE = 10
    CHILD_TICKET_PRICE = 5
    CONC_TICKET_PRICE = 8
    PREMIUM_FACTOR = 2
    EXTRAVAGANT_FACTOR = 5

    adultCost=numAdultTickets*ADULT_TICKET_PRICE
    childCost=numChildTickets*CHILD_TICKET_PRICE
    concCost=numConcTickets*CONC_TICKET_PRICE
    totalCost=adultCost+childCost+concCost

    if (packageCode=="P"):
        totalCost=totalCost* PREMIUM_FACTOR
    elif(packageCode=="E"):
        totalCost=totalCost*EXTRAVAGANT_FACTOR

    return totalCost

def main():
    quantity1 = getQuantity("Enter a value")
    total = calcTotalCost("P",quantity1,0,0)
    print(total)

main()