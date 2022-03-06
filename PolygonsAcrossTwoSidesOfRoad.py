#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:33:47 2022

@author: milesweedon
"""

"""
EXPLANATION OF ALGORITHM:
    

This third and final algorithm involves the postman posting to both sides of the road as he makes his way down the street.

The algorithm runs as follows:
    
    1) The postman starts off at the starting end of one street side.
    
    2) He then compares the distance to the closest lamppost on the streetside he's currently on, against the distance
       between himself and the closest lamppost on the opposite side of the road. This is shown in the diagram below:
       
       
        x                x             x
       ----------------------------------------                
                                        .                      Where:
                                         .                     O is the postman with his cart at the starting position.
                                          .                    x are the lampposts
                                           .                   The dotted lines are the two distances that the algorithm is comparing.
                                            .                  The dashed lines represent street sides.
                                             .
       ---------------------------------------O
              x               x . . . . . . . .


       Whichever distance is the shortest distance is the one the postman moves to with his cart.

    3) If the postman has chained his cart up to a lampost at horizontal distance 0m from the starting point, skip to part 4 of this discription.
    
       If the postman has chained his cart up to the starting lamppost and its not at horizontal distance 0m from the starting point, the postman
       analyses if there are any houses that are due post between the original starting position and the current horizontal position. If there are, he will
       deliver to these houses with the shortest distance possible - to do this the algorithm treats the houses as points, and forms a polygon 
       with the houses.
       If there are no houses due post, the algorithm moves to part 4 of this discription.
      
    4) The algorithm now finds the next closest lamppost, like in part two, only this time it only looks at the lampposts that are ahead of the current
       horizontal position. The algorithm then checks for any houses due post between the current horizontal position, and the next lampost, and delivers 
       to these houses in the shortest distance possible, before moving to the next lampost.
       
    5) The algorithm repeats this, until the algorithm finally checks for houses between the final lamppost and the end of the street, and delivers to
       these houses if required.
       
    6) The algorithm then returns the total distance travelled by the postman. 
    
    
NOTE:               Since the postman has a max sack capacity to carry the letters, the postman may do multiple trips to different houses whilst his 
                    cart is locked up to a lamppost. In other words, the algorithm also checks how much post is due at each house, and he'll leave his 
                    cart to deliver post to the houses if his sack becomes full with post. He may then end up making multiple trips if there is a lot 
                    of post due between two lampposts for instance.
    
ADDITIONAL NOTE:    The algorithm also constantly checks to see if there exists any lampposts on either side of the road. 
    
                    If, for example only one side of the road had lampposts, then the postman would work his way along this side of the road, from 
                    lamppost to lamppost.
          
                    If there exists no lampposts on either side of the road, then the postman would deliver to all houses between the start and end of 
                    the street in the shortest distance possible.

"""


from math import *



def PolygonsAcrossTwoSidesOfRoad(lamPosts, oppositeLamPosts, houseFrontsFromStart, oppositeHouseFrontsFromStart, letters, oppositeLetters, width, maxLetters):

    #Set some global variables from the above arguments, so that these can be used in later functions.
    global houseFrontsFromStartVar
    global oppositeHouseFrontsFromStartVar
    global lettersVar
    global oppositeLettersVar
    global widthVar
    global deliveryGoingBackwards
    houseFrontsFromStartVar = houseFrontsFromStart
    oppositeHouseFrontsFromStartVar = oppositeHouseFrontsFromStart
    lettersVar = letters
    oppositeLettersVar = oppositeLetters
    widthVar = width
    deliveryGoingBackwards = False  #To deal with special case as start, where the postman may be delivering to houses behing the carts position instead of ahead of the cart position.

    #Set the overall distance to zero. This variable below is what the function will return at the very end.
    totalDistance = 0

    #Calculate the number of houses on each side of the street
    global numberOfHouses
    global oppositeNumberOfHouses
    numberOfHouses = len(houseFrontsFromStart)
    oppositeNumberOfHouses = len(oppositeHouseFrontsFromStart)

    #Set a variable for each side of the road which tracks whether each house has been delivered to or not.
    global houseDeliveredTracker
    global oppositeHouseDeliveredTracker
    houseDeliveredTracker = ['N'] * numberOfHouses # Initialise to not having a delivery.
    oppositeHouseDeliveredTracker = ['N'] * oppositeNumberOfHouses # Also initialise the houses on the opposite side of the road to not having a delivery.


    #Calculate the length of the road - this will be equal to the longest street side.
    if houseFrontsFromStart[numberOfHouses - 1] >= oppositeHouseFrontsFromStart[oppositeNumberOfHouses - 1]:
        streetLength = houseFrontsFromStart[numberOfHouses - 1]
    else:
        streetLength = oppositeHouseFrontsFromStart[oppositeNumberOfHouses - 1]
    
    #Set a variable that'll be used to determine whether we're at the end of the street or not.
    global currentlyAtEndOfStreet
    currentlyAtEndOfStreet = False


    #Define a variable called sackCapacity. This is equal to how many letters the postman can carry.
    global sackCapacity
    sackCapacity = maxLetters


    #Use a variable that keeps track which side of the road the postman is on.
    global postmanOnOppositeSideOfRoad
    postmanOnOppositeSideOfRoad = False   


    #This is a variable that tracks the distance along the road from the starting position. This only tracks the horizontal distance from the starting position.
    global position
    position = 0     

   
    #Find the nearest lampost. This will either be the first lampost on the current side of the street, or the first on the opposite side.
    #Calculating the distance to the first lampost on the opposite side of the street involves using pythagoras, since the postman should be moving in a straight line across.
    
    if bool(lamPosts) and bool(oppositeLamPosts):     #These bool functions check whether any lampposts exist on either side of the road.
        if min(lamPosts) < sqrt((min(oppositeLamPosts)**2)+(widthVar**2)):
            position = min(lamPosts)
            totalDistance = totalDistance + min(lamPosts)
            lamPosts.remove(min(lamPosts))     #Remove the minimum lamppost, so the next minimum element (if one exists) will be the next lamppost.
        else:
            position = min(oppositeLamPosts)
            totalDistance = totalDistance + sqrt((min(oppositeLamPosts)**2)+(widthVar**2))
            postmanOnOppositeSideOfRoad = True
            oppositeLamPosts.remove(min(oppositeLamPosts))   #Remove the minimum lamppost, so the next minimum element (if one exists) will be the next lamppost.

    if bool(lamPosts) and bool(oppositeLamPosts) == False:
        position = min(lamPosts)
        totalDistance = totalDistance + min(lamPosts)
        lamPosts.remove(min(lamPosts))

    if bool(lamPosts) == False and bool(oppositeLamPosts):
        position = min(oppositeLamPosts)
        totalDistance = totalDistance + sqrt((min(oppositeLamPosts)**2)+(widthVar**2))
        postmanOnOppositeSideOfRoad = True
        oppositeLamPosts.remove(min(oppositeLamPosts))
        


    #If the first lampost is not at the starting position, then we may need to traverse back, since there may be houses between the starting position and the first lampost.
    if position != 0:
        deliveryGoingBackwards = True
        totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(0, position)

    
    #Now moving forwards:
        
    #This loop will only end once we have reached the end of the street.
    while True:
        
        deliveryGoingBackwards = False

        #Remove any lamposts that are at the same position as the cart, or behind. We only want to have lampposts in the lamppost lists that are ahead of the current carts position.
        if bool(lamPosts) and bool(oppositeLamPosts):
            while True:
                if position >= min(lamPosts):
                    lamPosts.remove(min(lamPosts))
                    
                if position >= min(oppositeLamPosts):
                    oppositeLamPosts.remove(min(oppositeLamPosts))

                if bool(lamPosts) and bool(oppositeLamPosts) and position < min(lamPosts) and position < min(oppositeLamPosts):
                    break

                if bool(lamPosts) == False or bool(oppositeLamPosts) == False:
                    break


        elif bool(lamPosts) and bool(oppositeLamPosts) == False:
            while True:
                if position >= min(lamPosts):
                    lamPosts.remove(min(lamPosts))

                if bool(lamPosts) == False:
                    currentlyAtEndOfStreet = True
                    break

                if position < min(lamPosts):
                    break


        elif bool(lamPosts) == False and bool(oppositeLamPosts):
            while True:
                if position >= min(oppositeLamPosts):
                    oppositeLamPosts.remove(min(oppositeLamPosts))

                if bool(oppositeLamPosts) == False:
                    currentlyAtEndOfStreet = True
                    break

                if position < min(oppositeLamPosts):
                    break

        #If no further lampposts exist, then we only need to check for any houses needing delivery between the end of the street and the current position.
        else:
            currentlyAtEndOfStreet = True



        #Now find next lamppost. If at end of street, the next lamppost will effectively be the end of the street.
        
        if currentlyAtEndOfStreet:
            totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, streetLength)
            break


        nextLampost = 0
        if bool(lamPosts) and bool(oppositeLamPosts):
            if postmanOnOppositeSideOfRoad:
                if (min(oppositeLamPosts) - position) < sqrt(((min(lamPosts) - position) ** 2) + (widthVar**2)):
                    nextLampost = min(oppositeLamPosts)
                    totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                    totalDistance = totalDistance + min(oppositeLamPosts)
                    position = nextLampost

                else:
                    nextLampost = min(lamPosts)
                    totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                    totalDistance = totalDistance + sqrt(((min(lamPosts) - position) ** 2) + (widthVar**2))
                    position = nextLampost
                    postmanOnOppositeSideOfRoad = False

            else:
                if (min(lamPosts) - position) < sqrt(((min(oppositeLamPosts) - position) ** 2) + (widthVar**2)):
                    nextLampost = min(lamPosts)
                    totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                    totalDistance = totalDistance + min(lamPosts)
                    position = nextLampost

                else:
                    nextLampost = min(oppositeLamPosts)
                    totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                    totalDistance = totalDistance + sqrt(((min(oppositeLamPosts) - position) ** 2) + (widthVar**2))
                    position = nextLampost
                    postmanOnOppositeSideOfRoad = True


        elif bool(lamPosts) and bool(oppositeLamPosts) == False:
            if postmanOnOppositeSideOfRoad:
                nextLampost = min(lamPosts)
                totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                totalDistance = totalDistance + sqrt(((min(lamPosts) - position) ** 2) + (widthVar**2))
                position = nextLampost
                postmanOnOppositeSideOfRoad = False

            else:
                nextLampost = min(lamPosts)
                totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                totalDistance = totalDistance + (min(lamPosts) - position)
                position = nextLampost
                postmanOnOppositeSideOfRoad = False


        elif bool(lamPosts) == False and bool(oppositeLamPosts):
            if postmanOnOppositeSideOfRoad:
                nextLampost = min(oppositeLamPosts)
                totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                totalDistance = totalDistance + (min(oppositeLamPosts) - position)
                position = nextLampost

            else:
                nextLampost = min(oppositeLamPosts)
                totalDistance = totalDistance + CheckForHousesNeedingDeliveryBetweenTwoPoints(position, nextLampost)
                totalDistance = totalDistance + sqrt(((min(oppositeLamPosts) - position) ** 2) + (widthVar**2))
                position = nextLampost
                postmanOnOppositeSideOfRoad = True

        else:
            continue


    return totalDistance



#This function below checks between two points for any houses needing delivery.
#It also sends off the postman to deliver before the letters exceed the max sack capacity.
#He will keep returning to the cart and deliver the letters as many times as required, so that the sacks capacity isn't exceeded, and so that all houses have their letters delivered to.

def CheckForHousesNeedingDeliveryBetweenTwoPoints(Point1, Point2):
    existsHouseSideA = False
    existsHouseSideB = False
    housesToDeliverToOnFirstStreetSide = []     #These two empty lists are used in the next function: they have houses needing deivery appended to them and are used to form the 'polygon' when the postman delivers, in order for him to deliver in the shortest time possible.
    housesToDeliverToOnOppositeStreetSide = []
    distanceBetweenTheTwoPoints = 0
    countTotal = 0  #countTotal is used to keep count of how many letters are in the sack. countA and countB are used alongside this variable in order to compare to the max sack capacity, and deciding when to send the postman off from the cart to deliver.
    countA = 0
    countB = 0

    #Begin moving forward:
    for i in range(Point1, Point2):

        #Check if there is a house on first side of the road.
        for x in range(0, numberOfHouses):
            if houseFrontsFromStartVar[x] == i:
                existsHouseSideA = True
                countA = lettersVar[x]
                positionInHouseDeliveredTracker = x


        #Now check if there is a house on opposite side of the road.
        for x in range(0, oppositeNumberOfHouses):
            if oppositeHouseFrontsFromStartVar[x] == i:
                existsHouseSideB = True
                countB = oppositeLettersVar[x]
                positionInOppositeHouseDeliveredTracker = x




        #Check if these houses should be inluded in the delivery. This involves both checking whether or not the house at hand has been delivered to already, and if the postman has enough avaliable space in his sack to drop off the letters.
        #Below are five different possible combinations:

        #Comb. 1:
        if existsHouseSideA == True and existsHouseSideB == True and houseDeliveredTracker[positionInHouseDeliveredTracker] == 'N' and oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] == 'N':
            if countTotal+countA+countB > sackCapacity:
                distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
                housesToDeliverToOnFirstStreetSide = []
                housesToDeliverToOnOppositeStreetSide = []
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                countTotal = countA + countB
                existsHouseSideA = False
                existsHouseSideB = False
            else:
                countTotal = countTotal + countA + countB
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                existsHouseSideA = False
                existsHouseSideB = False

        #Comb. 2 & 3. Produce same result.
        if existsHouseSideA == True and existsHouseSideB == False and houseDeliveredTracker[positionInHouseDeliveredTracker] == 'N':
            if countTotal+countA > sackCapacity:
                distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
                housesToDeliverToOnFirstStreetSide = []
                housesToDeliverToOnOppositeStreetSide = []
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                countTotal = countA
                existsHouseSideA = False
            else:
                countTotal = countTotal + countA
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                existsHouseSideA = False


        if existsHouseSideA == True and existsHouseSideB == True and houseDeliveredTracker[positionInHouseDeliveredTracker] == 'N' and oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] == 'Y':
            if countTotal+countA > sackCapacity:
                distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
                housesToDeliverToOnFirstStreetSide = []
                housesToDeliverToOnOppositeStreetSide = []
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                countTotal = countA
                existsHouseSideA = False
            else:
                countTotal = countTotal + countA
                houseDeliveredTracker[positionInHouseDeliveredTracker] = 'Y'
                housesToDeliverToOnFirstStreetSide.append(houseFrontsFromStartVar[positionInHouseDeliveredTracker])
                existsHouseSideA = False


        #Comb. 4 & 5. Produce same result.
        if existsHouseSideA == False and existsHouseSideB == True and oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] == 'N':
            if countTotal+countB > sackCapacity:
                distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
                housesToDeliverToOnFirstStreetSide = []
                housesToDeliverToOnOppositeStreetSide = []
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                countTotal = countB
                existsHouseSideB = False
            else:
                countTotal = countTotal + countB
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                existsHouseSideB = False


        if existsHouseSideA == True and existsHouseSideB == True and houseDeliveredTracker[positionInHouseDeliveredTracker] == 'Y' and oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] == 'N':
            if countTotal+countB > sackCapacity:
                distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
                housesToDeliverToOnFirstStreetSide = []
                housesToDeliverToOnOppositeStreetSide = []
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                countTotal = countB
                existsHouseSideB = False
            else:
                countTotal = countTotal + countB
                oppositeHouseDeliveredTracker[positionInOppositeHouseDeliveredTracker] = 'Y'
                housesToDeliverToOnOppositeStreetSide.append(oppositeHouseFrontsFromStartVar[positionInOppositeHouseDeliveredTracker])
                existsHouseSideB = False


        #Now in the instance that we come to point 2 and we have post to deliver:
        if i == Point2 - 1 and countTotal > 0:
            distanceBetweenTheTwoPoints = distanceBetweenTheTwoPoints + Deliver(housesToDeliverToOnFirstStreetSide, housesToDeliverToOnOppositeStreetSide)
            housesToDeliverToOnFirstStreetSide = []
            housesToDeliverToOnOppositeStreetSide = []
            countTotal = 0


    return distanceBetweenTheTwoPoints




#This function is called when the postman needs to deliver the letters.
#It calculates the distance travelled when walking to all the houses.
#It calculates the shortest distance by calculating the 'polygon' that connects all the houses being delivered to together.

def Deliver(FirstStreetSide, OppositeStreetSide):
    deliveryDistance = 0

    if deliveryGoingBackwards == False:
        
        if bool(FirstStreetSide) and bool(OppositeStreetSide):
    
            if postmanOnOppositeSideOfRoad:
                #Calculate the final diagonal back, as well as the distance between the lampost and the first house that needs delivering to.
                lastDiagonalDistanceTravelledByPostman = sqrt(((min(FirstStreetSide) - position)**2) + (widthVar**2))
                deliveryDistance = deliveryDistance + lastDiagonalDistanceTravelledByPostman + (min(OppositeStreetSide) - position)
    
            else:
                lastDiagonalDistanceTravelledByPostman = sqrt(((min(OppositeStreetSide) - position)**2) + (widthVar**2))
                deliveryDistance = deliveryDistance + lastDiagonalDistanceTravelledByPostman + (min(FirstStreetSide) - position)
    
    
            lengthTravelledOnFirstStreetSide = max(FirstStreetSide) - min(FirstStreetSide)
            lengthTravelledOnOppositeStreetSide = max(OppositeStreetSide) - min(OppositeStreetSide)
            deliveryDistance = deliveryDistance + lengthTravelledOnFirstStreetSide + lengthTravelledOnOppositeStreetSide
    
    
            #Now calculate the distance between the minimum element of the opposite street side (effectively one of the verticys of the 'polygon'), and the minimum element of the first street side (another verticy of the 'polygon'). This calculates one of the lengths of this 'polygon'.
            #We will then add this to the delivery distance
            if max(OppositeStreetSide) > max(FirstStreetSide):
                baseLength = max(OppositeStreetSide) - max(FirstStreetSide)
    
            else:
                baseLength = max(FirstStreetSide) - max(OppositeStreetSide)
    
            firstDiagonalDistanceTravelledByPostman = sqrt((baseLength**2)+(widthVar**2))
            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman
    
    
    
        if bool(FirstStreetSide) and bool(OppositeStreetSide) == False:
            if postmanOnOppositeSideOfRoad:
                firstDiagonalDistanceTravelledByPostman = sqrt(((min(FirstStreetSide) - position)**2) + (widthVar**2))
                lengthTravelledOnFirstStreetSide = max(FirstStreetSide) - min(FirstStreetSide)
                lastDiagonalDistanceTravelledByPostman = sqrt(((max(FirstStreetSide) - position)**2) + (widthVar**2))
    
            else:
                firstDiagonalDistanceTravelledByPostman = 0
                lengthTravelledOnFirstStreetSide = (max(FirstStreetSide) - position) * 2
                lastDiagonalDistanceTravelledByPostman = 0
    
            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman + lengthTravelledOnFirstStreetSide + lastDiagonalDistanceTravelledByPostman
    
        if bool(FirstStreetSide) == False and bool(OppositeStreetSide):
            if postmanOnOppositeSideOfRoad:
                firstDiagonalDistanceTravelledByPostman = 0
                lengthTravelledOnFirstStreetSide = (max(OppositeStreetSide) - position) * 2
                lastDiagonalDistanceTravelledByPostman = 0
    
            else:
                firstDiagonalDistanceTravelledByPostman = sqrt(((min(OppositeStreetSide) - position)**2) + (widthVar**2))
                lengthTravelledOnFirstStreetSide = max(OppositeStreetSide) - min(OppositeStreetSide)
                lastDiagonalDistanceTravelledByPostman = sqrt(((max(OppositeStreetSide) - position)**2) + (widthVar**2))
    
            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman + lengthTravelledOnFirstStreetSide + lastDiagonalDistanceTravelledByPostman
    
    else:
        if bool(FirstStreetSide) and bool(OppositeStreetSide):

            if postmanOnOppositeSideOfRoad:
                #Calculate the final diagonal back, as well as the distance between the lampost and the first house that needs delivering to.
                lastDiagonalDistanceTravelledByPostman = sqrt(((position - max(FirstStreetSide))**2) + (widthVar**2))
                deliveryDistance = deliveryDistance + lastDiagonalDistanceTravelledByPostman + (position - max(OppositeStreetSide))

            else:
                lastDiagonalDistanceTravelledByPostman = sqrt(((position - max(OppositeStreetSide))**2) + (widthVar**2))
                deliveryDistance = deliveryDistance + lastDiagonalDistanceTravelledByPostman + (position - max(FirstStreetSide))


            lengthTravelledOnFirstStreetSide = max(FirstStreetSide) - min(FirstStreetSide)
            lengthTravelledOnOppositeStreetSide = max(OppositeStreetSide) - min(OppositeStreetSide)
            deliveryDistance = deliveryDistance + lengthTravelledOnFirstStreetSide + lengthTravelledOnOppositeStreetSide


            #Now calculate the distance between the minimum element of the opposite street side (effectively one of the verticys of the 'polygon'), and the minimum element of the first street side (another verticy of the 'polygon'). This calculates one of the lengths of this 'polygon'.
            #We will then add this to the delivery distance
            if min(OppositeStreetSide) > min(FirstStreetSide):
                baseLength = min(OppositeStreetSide) - min(FirstStreetSide)

            else:
                baseLength = min(FirstStreetSide) - min(OppositeStreetSide)

            firstDiagonalDistanceTravelledByPostman = sqrt((baseLength**2)+(widthVar**2))
            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman



        if bool(FirstStreetSide) and bool(OppositeStreetSide) == False:
            if postmanOnOppositeSideOfRoad:
                firstDiagonalDistanceTravelledByPostman = sqrt(((position - max(FirstStreetSide))**2) + (widthVar**2))
                lengthTravelledOnFirstStreetSide = max(FirstStreetSide) - min(FirstStreetSide)
                lastDiagonalDistanceTravelledByPostman = sqrt(((position - min(FirstStreetSide))**2) + (widthVar**2))

            else:
                firstDiagonalDistanceTravelledByPostman = 0
                lengthTravelledOnFirstStreetSide = (position - min(FirstStreetSide)) * 2
                lastDiagonalDistanceTravelledByPostman = 0

            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman + lengthTravelledOnFirstStreetSide + lastDiagonalDistanceTravelledByPostman

        if bool(FirstStreetSide) == False and bool(OppositeStreetSide):
            if postmanOnOppositeSideOfRoad:
                firstDiagonalDistanceTravelledByPostman = 0
                lengthTravelledOnFirstStreetSide = (position - min(OppositeStreetSide) * 2)
                lastDiagonalDistanceTravelledByPostman = 0

            else:
                firstDiagonalDistanceTravelledByPostman = sqrt(((position - max(OppositeStreetSide))**2) + (widthVar**2))
                lengthTravelledOnFirstStreetSide = max(OppositeStreetSide) - min(OppositeStreetSide)
                lastDiagonalDistanceTravelledByPostman = sqrt(((position - min(OppositeStreetSide))**2) + (widthVar**2))

            deliveryDistance = deliveryDistance + firstDiagonalDistanceTravelledByPostman + lengthTravelledOnFirstStreetSide + lastDiagonalDistanceTravelledByPostman


    return deliveryDistance

