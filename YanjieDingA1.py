priceList = []
def getMenuChoice(userName):
    """
    menuChoice = str(input("This ticket is for :  (Y)ou  (S)omeone else  "))
    while not ( menuChoice == "Y" or menuChoice == "S" ):
        print("Error message")
        menuChoice = str(input("This ticket is for :  (Y)ou  (S)omeone else  "))
    if menuChoice == "Y":
        getTicketFor = userName
    else:
        getTicketFor = str(input("Please enter the name of the person travelling"))

    :param userName: The user's name
    :return: getTicketFor
    """

def getRoundTrip():
    """
    roundTrip = str(input("Is this a return trip (R) or One-Way (O): "))
    while roundTrip != "R" and roundTrip != "O":
        print("Error message")
        roundTrip = str(input("Is this a return trip (R) or One-Way (O): "))
    if roundTrip is "R":
        trip = "Return"
    else:
        trip = "One-Way"
    :return: trip
    """

def getDestination(trip):
    """
     if trip == "Return":
        print ("(C)airns – $400 (S)ydney – $575 (P)erth - $700")
        Tripdestination = str(input("Please select the destination for your return trip."))
        while not (Tripdestination == "C" or Tripdestination == "S" or Tripdestination == "P"):
            print("Error message")
            Tripdestination = str(input("Please select the destination for your return trip."))
        if Tripdestination is "C":
            destination = "Cairns"
        else:
            if Tripdestination is "S":
                destination = "Sydney"
            else:
                if Tripdestination is "P":
                    destination = "Perth"
    else:
        if trip == "One-Way":
            print("(C)airns – $250 (S)ydney – $420 (P)erth - $510")
            Tripdestination = str(input("Please select the destination for your One-Way trip."))
            while not (Tripdestination == "C" or Tripdestination == "S" or Tripdestination == "P"):
                print("Error message")
        if Tripdestination is "C":
            destination = "Cairns"
        else:
            if Tripdestination is "S":
                destination = "Sydney"
            else:
                if Tripdestination is "P":
                    destination = "Perth"
    :param trip: User choose "Return" or "One-Way"
    :return: destination
    """

def getFare():
    """
    print("Please choose the type of fare: ")
    print("Fees are displayed below and are in addition to the basic fare. Please note choosing Frugal fare means you will not be offered a seat choice.")
    Seatfare = str(input("(B)usiness - $275 (E)conomy - $25 (F)rugal - $0"))
    while not (Seatfare =="B" or Seatfare =="E" or Seatfare =="F"):
        print("You must enter a valid value")
        print("Please enter option:")
        Seatfare = str(input("Please choose the type of fare: "))
    if Seatfare is "B":
        fare = "Business"
    else:
        if Seatfare is "E":
            fare = "Economy"
        else:
            if Seatfare is "F":
                fare = "Frugal"
    :return: fare
    """

def getSeat():
    """
    print ("Please choose the seat type: ")
    seatType = str(input(" (W)indow - $75 (A)isle - $50 (M)iddle - $25 "))
    while not(seatType == "W" or seatType == "A" or seatType == "M"):
        print("You must enter a valid value")
        print("Please enter option:")
        seatType = str(input("Please choose the seat type: "))
    if seatType is "W":
        seat = "Window"
    else:
        if seatType is "A":
            seat = "Aisle"
        else:
            if seatType is "M":
                seat = "Middle"
    :return: seat
    """

def getDestinationPrice(destination, trip):
    """
    if trip is "Return":
        if destination is "Cairus":
            Destinationprice = 400
        else:
            if destination is "Sydney":
                Destinationprice = 575
            else:
                Destinationprice = 700
    else:
        if trip is "One-Way":
            if destination is "Cairus":
                Destinationprice = 250
            else:
                if destination is "Sydney":
                    Destinationprice = 420
                else:
                    if destination is "Perth":
                        Destinationprice = 510
    :param destination:
    :param trip:
    :return: Destinationprice
    """
    if trip is "Return":
        if destination is "Cairus":
            Destinationprice = 400
        else:
            if destination is "Sydney":
                Destinationprice = 575
            else:
                Destinationprice = 700
    else:
        if trip is "One-Way":
            if destination is "Cairus":
                Destinationprice = 250
            else:
                if destination is "Sydney":
                    Destinationprice = 420
                else:
                    if destination is "Perth":
                        Destinationprice = 510
    return Destinationprice

def getFarePrice(fare):
    """
    if fare is "Business":
        farePrice = 275
    else:
        if fare is "Economy":
            farePrice = 25
        else:
            if fare is "Frugal":
                farePrice = 0
    :param fare: The type of fare
    :return: farePrice
    """

def getSeatPrice(seat):
    """
    if seat is "Window":
        seatPrice = 75
    else:
        if seat is "Aisle":
            seatPrice = 25
        else:
            if seat is "Middle":
                seatPrice = 0
    :param seat: The type of seat
    :return: seatPrice
    """

def calcTotalPrice(Destinationprice, farePrice, seatPrice):
    """
    totalFee = Destinationprice + farePrice + seatPrice
    :param Destinationprice: The price of trip
    :param farePrice: The price of fare
    :param seatPrice: The price of seat type
    :return: totalFee
    """

def getDiscount(age):
    """
        dicount = 0
    if age >= 0 and age < 16:
        print("Get 50% discounted")
        dicount = 0.5
    else:
        if age > 16:
            print ("No discounted")
            dicount = 1
    :param age: The age of traveler
    :return: dicount
    """

def finalOrder(age, totalFee):
    """
    finalFee = 0
    if age >= 0 and age < 16:
        finalFee = totalFee * 0.5
    else:
        if age > 16:
            finalFee = totalFee
    :param age: the age of traveller
    :param totalFee: the total price of price
    :return: finalFee
    """

def main():
    destinationPrice = 0
    seatChoicePrice = 0
    seatTypePrice = 0
    destinationChoose = ""
    print("Welcome to the ordering system.")
    print("Please enter your using name.")
    Name = input()
    print("Welcome " + Name)
    print("Tropical Airlines Ticket Ordering System.")
    print("(I)nformation")
    print("(O)rder ticket")
    print("(E)xit")
    print("Please enter option:")

    getMenuChoice = input()
    while getMenuChoice == "I":
        print("Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.")
        print("Tropical Airlines Ticket Ordering System.")
        print("(I)nformation")
        print("(O)rder ticket")
        print("(E)xit")
        print("Please enter option:")
        getMenuChoice = input()
    if getMenuChoice == "O":
        print(Name + ", is this for:")
        print("(Y)ou")
        print("(S)omeone else")
        getTicketFor = input()
        while getTicketFor not in "YS":
            print("You must enter a valid value")
            print("Please enter option:")
            getTicketFor = input()
        if getTicketFor == "S":
            print("Please enter the name of the person travelling")
            Name = input()
            print("This ticket is for", Name)
        print("Is this a return trip (R) or One-Way (O) ")
        roundTrip = input()
        if roundTrip == "R" or roundTrip == "O":
            if roundTrip == "R":
                print("Please select the destination for your return trip. Fare prices are listed below.")
                print("(C)airns – $400")
                print("(S)ydney – $575")
                print("(P)erth- $700")
                getDestination = input()
                if getDestination == "C" or getDestination == "S" or getDestination == "P":
                    if getDestination == "C":
                        destinationChoose = "Cairns(return) – $400"
                        destinationPrice = 400
                        print("Cairns(return) – $400")
                    else:
                        if getDestination == "S":
                            destinationChoose = "Sydney(return) – $575"
                            destinationPrice = 575
                            print("Sydney(return) – $575")
                        else:
                            if getDestination == "P":
                                destinationChoose = "Perth(return) - $700"
                                destinationPrice = 700
                                print("Perth(return) - $700")
                while getDestination not in "CSP":
                    print("You must enter a valid value")
                    print("Please enter option:")
                    getDestination = input()
            else:
                if roundTrip == "O":
                    print("Please select the destination for your trip. Fare prices are listed below.")
                    print("(C)airns – $250")
                    print("(S)ydney – $420")
                    print("(P)erth - $510")
                    getDestination = input()
                    if getDestination == "C" or getDestination == "S" or getDestination == "P":
                        if getDestination == "C":
                            destinationChoose = "Cairns(one-way) – $250"
                            destinationPrice = 250
                            print("Cairns(one-way) – $250")
                        else:
                            if getDestination == "S":
                                destinationChoose = "Sydney(one-way) – $420"
                                destinationPrice = 420
                                print("(S)ydney(one-way) – $420")
                            else:
                                if getDestination == "P":
                                    destinationChoose = "Perth(one-way) - $510"
                                    destinationPrice = 510
                                    print("Perth(one-way) - $510")
                    while getDestination not in "CSP":
                        print("You must enter a valid value")
                        print("Please enter option:")
                        getDestination = input()
        while roundTrip not in "RO":
            print("You must enter a valid value")
            print("Please enter option:")
            roundTrip = input()

        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. ")
        print("Please note choosing Frugal fare means you will not be offered a seat choice.")
        print("(B)usiness  275")
        print("(E)conomy  25")
        print("(F)rugal  0")
        getSeatChoice = input()
        if getSeatChoice == "B" or getSeatChoice == "E" or getSeatChoice == "F":
            if getSeatChoice == "B":
                seatChoicePrice = 275
                print("(B)usiness   275")
            else:
                if getSeatChoice == "E":
                    seatChoicePrice = 25
                    print("(E)conomy  25")
                else:
                    if getSeatChoice == "F":
                        seatChoicePrice = 0
                        print("(F)rugal  0")
        while getSeatChoice not in "BEF":
            print("You must enter a valid value")
            print("Please enter option:")
            getSeatChoice = input()
        print("Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.")
        print("(W)indow  75")
        print("(A)isle   50")
        print("(M)iddle  (-25) ")
        getSeatType = input()
        if getSeatType == "W" or getSeatType == "A" or getSeatType == "M":
            if getSeatType == "W":
                seatTypePrice = 75
                print("(W)indow  75")
            else:
                if getSeatType == "A":
                    seatTypePrice = 50
                    print("(A)isle   50")
                else:
                    if getSeatType == "M":
                        seatTypePrice = (-25)
                        print("(M)iddle  (-25) ")
        while getSeatType not in "WAM":
            print("You must enter a valid value")
            print("Please enter option:")
            getSeatType = input()
        print("How old is the person travelling. Travellers under 16 years old will receive a 50% discount for the child fare.")

        Totalcost = calcTotalPrice(destinationPrice, seatChoicePrice, seatTypePrice)
        print(Totalcost)
        age = int(input())
        calcTotalFee = 0
        if age < 16 and age > 0:
            calcTotalFee = (destinationPrice + seatChoicePrice + seatTypePrice) * 0.5
        else:
            calcTotalFee = destinationPrice + seatChoicePrice + seatTypePrice

        priceList.append(calcTotalFee)
        print("Ticket for: ", Name)
        print("Destination: ", destinationChoose)
        print("Fare: ", seatChoicePrice)
        print("Seat type: ", seatTypePrice)
        print("Age: ", age)
        print("Total Price: ", calcTotalFee)
        print("Tropical Airlines Ticket Ordering System")


    while getMenuChoice not in "IEO":
        print("You must enter a valid value")
        print("Please enter option:")
        getMenuChoice = input()

    if getMenuChoice == "E":
        extend()

main()

def extend():
    main()
    print("Please type your using name again.")
    print("We need to confirm")
    print("Thank you")
    Name = input()
    print(Name, " your orders are:  ")
    for calcTotalFee in priceList:
        print("$", calcTotalFee)
    print("Your final total is:" "$", sum(priceList))
    print("Thank you for visting Tropical Airlines.")

extend()









