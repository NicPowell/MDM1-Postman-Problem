# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:50:09 2022

@author: lewis
"""
"""
This model is slightly different from the next lamp post version. 
This instead will, excluding houses with no mail to be delivered too, will 
create a dictionary. The keys are the lamp post's index, and values are a set 
of lists of the house index's. It puts each house index with the lamp post that
is closest to it. 
The postman will then lock up at the first lamp post, and then deliver to all 
houses closest to that lamp post. Does this till all of these closest houses
are delivered too, then he will move the cart to the next post and do the same
thing. Once this cycle is completed for all lamposts, he will return to the 
cart and move it to the end of the road. 

Algoritm order:
     (1) setup initial checks
     (2) lock cart on next lamp post and deliver to closet houses
             #note steps 3 and 4 are repeated for each lamp post
     (3) deliver to houses (using max letters that can be carried)
          - If maximum letters is reached
            (a) go back to cart tp get more letters 
            (b) go to next delivery house
            (else he is able to deliver to all closest houses to post so does 
             all these before (4)). 
     (4) walk back to cart 
     (5) get to end of road from last cart lockup
     
     
------------------------------------------------------------------------------
"""

from collections import defaultdict
from Logger import *

def singleSideStreetDeliveryNearestLampPost (maxLetters,lampPostsPositionList, houseFrontsList, houseLettersList):
    
    # __________ (1) setup initial checks etc __________    
    # calculate some 'totals' ...
    numberOfHouses = len(houseFrontsList)
    streetLength = sum (houseFrontsList)
    lettersToBeDelivered = sum (houseLettersList) 
    log("****************************************************************************")
    log("Number of Houses " + str(numberOfHouses))
    log("Number of letters for street " + str(lettersToBeDelivered))
    log("Street Length " + str(streetLength))
    log("****************************************************************************")
    
    # ... check supplied data is as expected ...
    if max(houseLettersList) > maxLetters:
        log ("House delivery greater than max letters in bag not supported")
        return
    if len(houseLettersList) != len(houseFrontsList):
        log ("houseLettersList size different to HouseFront Size")
        return
    if lettersToBeDelivered == 0:
        log("No letters to deliver. Going to end of street")
        log("Total Distance Travelled is "+ streetLength)
        return
    if len(lampPostsPositionList) == 0:
        log("We require at least one point to lock cart")
        return

    
    # ... initialise some parameters ...
    lettersDelivered = 0
    cartPosition = 0
    houseDeliveredTracker = ['N'] * numberOfHouses # initialise to not having a delivery
    distanceTravelled = 0
    
    # finding the nearest lamp post for each house, and then putting it into a dictionary 
    #gives result of the lamp post key with value of a list of house indexes 
    nearestLampPostDict = defaultdict(list) 
    for houseIndex in range(0, numberOfHouses):
        if houseLettersList[houseIndex] == 0:
            continue
        distanceToDeliveryPoint = calcHouseFrontEndPosition (houseFrontsList, houseIndex)
        lampPostIndex = findNearestLampPostIndex(lampPostsPositionList, distanceToDeliveryPoint)
        nearestLampPostDict[lampPostIndex].append(houseIndex)
    log(nearestLampPostDict)
    
    
    # ... Now into algoritm
    # __________ (2) lock cart on next lamp post and deliver to closet houses __________  
    for lampPostIndex, houseIndexList in nearestLampPostDict.items():
        #lock cart to next lamp post
        lampPostsPosition = lampPostsPositionList[lampPostIndex]
        distanceTravelled = distanceTravelled + abs(lampPostsPosition - cartPosition)
        cartPosition = lampPostsPosition 
        
        # move to house delivery point(the door taken to be at the end of the house's width)
        #note that distanceToHouse below is distance from 0m to door of the house 
        #use houseIndexList[0] as want to go to first element of the list(the first house)
        distanceToHouse = calcHouseFrontEndPosition(houseFrontsList, houseIndexList[0]) 
        distanceTravelled = distanceTravelled + abs(cartPosition - distanceToHouse)
        log ("*** Total Distance Travelled (to house delivery point): " + str(distanceTravelled))

        # __________ (3) deliver to houses (using max letters that can be carried) __________              
        # deliver letters up to max in post bag. returns 'number of letters delivered' and 'distance walked'
        result = deliverLettersForCloseHouses (houseFrontsList, houseDeliveredTracker, houseLettersList, maxLetters, houseIndexList, cartPosition)
        lettersDeliveredForCloseHouses = result[0]
        lettersDelivered = lettersDelivered + lettersDeliveredForCloseHouses
        distanceTravelled = distanceTravelled + result[1]
        lastHouseDeliveredIndex = result[2]
        #log ("Distance covered delivering letters: " + str(result[1]))
        log ("*** Total Distance Travelled (after delivering all letters): " + str(distanceTravelled))
    
    
        # __________ (4) walk back to cart___________________
        distanceToCart = calculateDistanceBetweenHouseAndCart(houseFrontsList, cartPosition, lastHouseDeliveredIndex)
        distanceTravelled = distanceTravelled + distanceToCart
        log ("*** Total Distance Travelled (back to cart): " + str(distanceTravelled))
        
    #__________(5) get to end of road from last cart lockup_____________
    distanceTravelled = distanceTravelled + abs(streetLength - cartPosition)
    log ("*** Total Distance Travelled (end of street): " + str(distanceTravelled))
        
    
    return distanceTravelled
    


"""
calculate the position for next delivery
return - the position for delivery for a house -the door (e.g. at the end of the property)
"""
def calcHouseFrontEndPosition (houseFrontsList, houseIndex):
    distance = sum(houseFrontsList[0:houseIndex+1])
    #log("Distance to house delivery point of index " + str(houseIndex) + " is " + str(distance))
    return distance

def findNearestLampPostIndex(lampPostsPositionList, distanceToDeliveryPoint):
    nearestLampPostIndex = -1
    minDistance = 1000000
    distanceBetweenHouseAndLampPost = 0
        
    for lampPostIndex, lampPostPosition in enumerate(lampPostsPositionList):
        distanceBetweenHouseAndLampPost = abs(lampPostPosition - distanceToDeliveryPoint)
        #log(distanceBetweenHouseAndLampPost)
        if distanceBetweenHouseAndLampPost < minDistance:
            minDistance = distanceBetweenHouseAndLampPost 
            nearestLampPostIndex = lampPostIndex 
    log("min distance " + str(minDistance))
    return nearestLampPostIndex

"""
once at first house in list of houses to deliver to (for particular lamp post),
we need to deliver to these houses. 

"""
def deliverLettersForCloseHouses (houseFrontsList, houseDeliveredTracker, houseLettersList, maxLetters, houseIndexList, cartPosition):
    firstHouse = True # at first house as have walked from cart to the door
    distanceTravelledForClosestHouses = 0
    lettersDelivered = 0
    lettersInBag = 0
    #log ("Delivery run start House " + str(nextHouseIndex))
    previousHouseIndex = 0
    for nextHouseIndex in houseIndexList:
        houseDeliveredTracker[nextHouseIndex] = 'Y'
        lettersForHouse = houseLettersList[nextHouseIndex]
        if (lettersInBag + lettersForHouse) <= maxLetters:
            lettersInBag = lettersInBag + lettersForHouse
            lettersDelivered = lettersDelivered + lettersForHouse
            if firstHouse: # start at delivery position for first house sono walking
                firstHouse = False
            else:
                distanceTravelledForClosestHouses = distanceTravelledForClosestHouses + calculateDistanceBetweenPreviousAndNextHouse (houseFrontsList, previousHouseIndex, nextHouseIndex)
            log ("Delivered " + str(houseLettersList[nextHouseIndex]) + " letters to house index " + str(nextHouseIndex))
            log ("Distance Travelled For Closest Houses " + str(distanceTravelledForClosestHouses))
        else: # more than maxLetters
            log ("MAX LETTERS REACHED")
            # (3a)Move back to cart from house
            distanceToCart = calculateDistanceBetweenHouseAndCart(houseFrontsList, cartPosition, previousHouseIndex)
            distanceTravelledForClosestHouses = distanceTravelledForClosestHouses + distanceToCart
            # (3b) Move to next house from cart
            distanceToNextHouse = calculateDistanceBetweenHouseAndCart(houseFrontsList, cartPosition,nextHouseIndex)
            distanceTravelledForClosestHouses = distanceTravelledForClosestHouses + distanceToNextHouse
            lettersInBag =  lettersForHouse
            log ("Delivered " + str(houseLettersList[nextHouseIndex]) + " letters to house index " + str(nextHouseIndex))
            log ("Distance Travelled For Closest Houses " + str(distanceTravelledForClosestHouses))
        previousHouseIndex =  nextHouseIndex
            
    #log ("Delivery run end House " + str(nextHouseIndex) + " delivering " + str(lettersDelivered) + " letters")
    return  lettersDelivered, distanceTravelledForClosestHouses, nextHouseIndex  

"""

"""
def calculateDistanceBetweenHouseAndCart(houseFrontsList, cartPosition, houseIndex):
    deliveryPosition = calcHouseFrontEndPosition(houseFrontsList, houseIndex)
    return abs(cartPosition - deliveryPosition)


def calculateDistanceBetweenPreviousAndNextHouse (houseFrontsList, previousHouseIndex, nextHouseIndex):
    distance = 0

    # range not to include previous house but include nexthouse
    for i in range (previousHouseIndex+1, nextHouseIndex+1):
        distance = distance + houseFrontsList[i]
    return distance


        
    