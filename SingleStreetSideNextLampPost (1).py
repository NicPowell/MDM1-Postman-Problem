# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:52:38 2022

@author: lewis
"""

"""
-------------------------------------------------------------------------------
Description
-------------------------------------------------------------------------------
This algorithm has the postman moving along one side of the street
delivering letters in house order.
It will move the cart to the next lamp post when the postman reaches it.

A check will happen to see if the cart needs to move before maximum letters
are picked up if some houses do not need letters delivered.

Basic algorithm follows : 
     (1) setup initial checks
     (2) lock cart on initial lamp post and go to first delivery house
     (3) deliver to houses (using max letters that can be carried)
     (4) walk back to cart
     (5) check to see if we want to move cart to new lamp post
     (6) move to next house for delivery 
     (7) go back to step (3) if more deliveries OR go to step (6) if no move to be delivered
     (8) go to end of street

NOTES:
    - Currently does not allow the number of letters for any house to be greater than that can be carried

-------------------------------------------------------------------------------
Common Attributes used in algorithm
-------------------------------------------------------------------------------
maxLetters:                maximum number of letters that can be carried (in post bag!)
houseLettersList:          number of letters to be delivered to each house (no delivery requires 0)  
houseFrontsList:           width of each house(property) 
lampPostsPositionList:     position of each lamp post(cart lockup point). each position in the list is the distance from the beginning of the side of the street
numberOfHouses:            obvious! each 'list' above should have this size
streetLength:              obvious! all the 'house fronts' on one side should equal this
lettersToBeDelivered       total number of letters to be delivered
lettersDelivered:          number of letters that HAVE been 'currently' delivered
houseDeliveredTracker:     lists the houses that have had OR not had a deliver
lastDeliveredHouseIndex:   the number/index of the house on the side of the street that was delivered to last. range 0 to numberOfHouses-1
nextDeliveryHouseIndex:    the number/index of the house on the side of the street that will be delivered to next. range 0 to numberOfHouses-1
lastDeliveryHouseOnStreet: the number/index of the 'last house' on the side of the street that will be delivered. range 0 to numberOfHouses
cartPosition:              where the cart is locked - this will be one of the lamp post position. this is a distance relative to the starting end of the street  
nextHousePosition:         distance relative to the starting end of the street of the next House (nextDeliveryHouseIndex)
distanceTravelled:         running total of the distance travelled during delivery

"""
from Logger import *

"""
main function to invoke to use the algorithm to calculate the distance travelled for the side of the street
returns -  the total distance travelled
"""
def singleSideStreetDeliveryNextLampPost (maxLetters,lampPostsPositionList, houseFrontsList, houseLettersList):
    
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
    lastDeliveredHouseIndex = -1 # no deliveries yet
    
    # ... check last house and first houses that require a delivery
    nextDeliveryHouseIndex = findnextDeliveryHouseIndex (houseLettersList,lastDeliveredHouseIndex)
    lastDeliveryHouseOnStreet = findLastDeliveryHouseIndexOnStreet(houseLettersList)
    
    # __________ (2) lock cart on initial lamp post and go to first delivery house __________  
    # find first lamp post to use ...
    nextHousePosition = calcHouseFrontEndPosition (houseFrontsList, nextDeliveryHouseIndex)
    result = findNextCartPosition (lampPostsPositionList, cartPosition, nextHousePosition)
    distanceTravelled = result[0]
    cartPosition = result [1]
    # ... return to first delivery house
    distanceToHouse = abs(cartPosition - calcHouseFrontEndPosition (houseFrontsList, nextDeliveryHouseIndex))
    distanceTravelled = distanceTravelled + distanceToHouse
    
    # Output some initial stats
    log ("Cart Locked at position:  " + str(cartPosition));
    log ("First House to deliver is: " + str(nextDeliveryHouseIndex))
    log ("Total Distance Travelled:  " + str(distanceTravelled))
    
    # repeat delivering letters in stages based on number of letters that can be carries [steps (3) to (6) in the steps in description above]
    while lettersDelivered < lettersToBeDelivered:
        
        # __________ (3) deliver to houses (using max letters that can be carried) __________              
        # deliver letters up to max in post bag. returns 'number of letters delivered' and 'distance walked'
        result = deliverLettersFromBag (houseFrontsList, houseDeliveredTracker, houseLettersList, maxLetters, 
                                        lastDeliveryHouseOnStreet, nextDeliveryHouseIndex, lampPostsPositionList, cartPosition, lastDeliveredHouseIndex)
        lettersInBag = result[0]
        lettersDelivered = lettersDelivered + lettersInBag
        distanceTravelled = distanceTravelled + result[1]
        log ("Distance covered delivering letters: " + str(result[1]))
        log ("*** Total Distance Travelled (delivered letters): " + str(distanceTravelled))
        lastDeliveredHouseIndex = result[2] 
     
        # __________ (4) walk back to cart  __________
        # back to cart for more letters
        distToCart = moveToCart (houseFrontsList, cartPosition, lastDeliveredHouseIndex)
        log("Distance to cart: " + str(distToCart))
        distanceTravelled = distanceTravelled + distToCart
        log ("*** Total Distance Travelled (walk back to cart) " + str(distanceTravelled))
        
        # __________ (5) check to see if we want to move cart to new lamp post __________
        # calculate the distance to the next house that has a delivery ...
        nextDeliveryHouseIndex = findnextDeliveryHouseIndex (houseLettersList,lastDeliveredHouseIndex)
        if (nextDeliveryHouseIndex == None ):
            break # all letters delivered so going to step (8) below
        nextHousePosition = calcHouseFrontEndPosition(houseFrontsList,nextDeliveryHouseIndex)
        # ... move cart closer to next house if required
        log("Check for a cart move") 
        result = findNextCartPosition (lampPostsPositionList, cartPosition, nextHousePosition)
        distanceTravelled = distanceTravelled + result[0]
        cartPosition = result [1]
        log ("*** Total Distance Travelled (move cart) " + str(distanceTravelled))
 
        # __________ (6) move to next house for delivery __________
        log("Move to next house. "+ str(nextDeliveryHouseIndex))
        distanceToNextHouse = abs(cartPosition - nextHousePosition)
        distanceTravelled = distanceTravelled + distanceToNextHouse
        log ("*** Total Distance Travelled (walk to house): " + str(distanceTravelled))
        
        # __________ (7) end of delivery stage. deliver more letters. back to while loop __________
     
    # __________ (8) go to end of street ___________    
    log("//////////////////// Finished  //////////////////////////////")
    log("Move cart to end of street.")
    if streetLength > cartPosition:
        # should be at cart here
        distanceTravelled = distanceTravelled + streetLength - cartPosition
        log ("*** Total Distance Travelled (walk to end of street) " + str(distanceTravelled))
    log("Trakcer: " + str(houseDeliveredTracker))
    log("/////////////////////////////////////////////////////////////")
    return distanceTravelled
    
""" 
 Deliver letters - Up to the maximum number of letters to be carried, deliveries are made to houses

 If the next house (that could be a block of houses) has no letters to be delivered there is a check 
 to see if it the cart should be moved rather than walking to far away from the locked cart. Likely to to shorter
 to deliver less and move the cart closer to the far away delivery.

 returns lettersDelivered, distanceTravelledForCurrentPostBag, lastDeliveredHouseIndex
 """
def deliverLettersFromBag (houseFrontsList, houseDeliveredTracker, houseLettersList, maxLetters, lastDeliveryHouseOnStreet, nextHouseIndex, lampPostsPositionList, cartPosition, lastDeliveredHouseIndex):

    firstHouse = True
    distanceTravelledForCurrentPostBag = 0
    lettersInBag = 0
    log ("Delivery run start House " + str(nextHouseIndex))
    while (nextHouseIndex <= lastDeliveryHouseOnStreet):
        lettersForHouse = houseLettersList[nextHouseIndex]
        # we have a house with no deliveries. this could be a block of houses so check if we should move the cart.
        if lettersForHouse == 0:
            needToMoveCart = checkIfShorterToMoveCart(houseLettersList, houseFrontsList, lampPostsPositionList, lastDeliveredHouseIndex, cartPosition)
            #log("Need to move cart: " + str(needToMoveCart))
            if needToMoveCart or needToMoveCart == None or lettersInBag == maxLetters:
                break
        else:
            houseDeliveredTracker[nextHouseIndex] = 'Y'
        
        if (lettersInBag + lettersForHouse) <= maxLetters:
            lettersInBag = lettersInBag + lettersForHouse
            if firstHouse: # start at delivery position for first house sono walking
                firstHouse = False
            else:
                distanceTravelledForCurrentPostBag = distanceTravelledForCurrentPostBag + houseFrontsList[nextHouseIndex]
            #log ("Delivered " + str(houseLettersList[nextHouseIndex]) + " letters to house index " + str(nextHouseIndex))
            #log ("Distance Travelled For Current Post Bag " + str(distanceTravelledForCurrentPostBag))
            lastDeliveredHouseIndex = nextHouseIndex
        else:
            break
        nextHouseIndex = nextHouseIndex + 1
    log ("Delivery run end House " + str(lastDeliveredHouseIndex) + " delivering " + str(lettersInBag) + " letters")
    return lettersInBag, distanceTravelledForCurrentPostBag, lastDeliveredHouseIndex    

"""
  decide whether to move cart or deliver more letters
  this check is called in the delivery function where there is a house that has no letters to be delivered
  this could be a block of houses so if may be beneficial to move the cart to a lamp post nearer the next delivery house
  return - boolean to indicate if the cart should move (None if no more deliveries)
"""
def checkIfShorterToMoveCart(houseLettersList, houseFrontsList, lampPostsPositionList, lastDeliveredHouseIndex, cartPosition):
    nextDeliveryHouseIndex = findnextDeliveryHouseIndex (houseLettersList,lastDeliveredHouseIndex)
    if (nextDeliveryHouseIndex == None ):
        return None
    nextHousePosition = calcHouseFrontEndPosition(houseFrontsList, nextDeliveryHouseIndex)
    nextPostIndex = lampPostsPositionList.index(cartPosition) +1
    if len(lampPostsPositionList) >  nextPostIndex and nextHousePosition >= lampPostsPositionList[nextPostIndex]:
        return True
    return  False

"""
 Walk to cart from current house delivered and calculate the distance
 return - distanceToCart
"""
def moveToCart (houseFrontsList, cartPosition, lastDeliveredHouseIndex):
    lastHouseDistance = calcHouseFrontEndPosition (houseFrontsList, lastDeliveredHouseIndex)
    return abs(cartPosition - lastHouseDistance)

"""
  Find next house that has a  delivery 
  return - the 'house index' OR 'None'
"""
def findnextDeliveryHouseIndex (houseLettersList,lastDeliveredHouseIndex):
    for i in range (lastDeliveredHouseIndex+1, len(houseLettersList)):
        if (houseLettersList[i] > 0):
            return i;
    return None;

"""
 Determine next lamp post to tie cart to based on next house to deliver
 this chooses the next lamp post that is closest to the next house that requires a delivery
 The lamp post may be before or after the house position
 
 return - 'distance to move cart' 'new cart position'
"""
def findNextCartPosition (lampPostsPositionList, cartPosition, nextHousePosition):
    movePosition = 0
    minDistanceBetweenHouseAndCart = 10000000000 # initialise with large number
    # for loop to find closest lamp post 
    for lampPostPosition in lampPostsPositionList:
        distance = abs(nextHousePosition - lampPostPosition)
        if distance < minDistanceBetweenHouseAndCart:
            minDistanceBetweenHouseAndCart = distance
            movePosition = lampPostPosition     
    if movePosition > 0 and movePosition > cartPosition:
        cartMoveDistance = movePosition - cartPosition
        #log ("Moving Cart up to " + str(movePosition) + " distance " + str(cartMoveDistance))
        return cartMoveDistance, movePosition 
    else:
        #log ("No Cart Move")     
        return 0, cartPosition # return original position   
"""
 calculate the position for next delivery
 return - the position for deliver for a house (e.g. at the end of the property)
"""
def calcHouseFrontEndPosition (houseFrontsList, houseIndex):
    return sum(houseFrontsList[0:houseIndex+1])
"""
   search for the last house on the street that has a delivery
"""
def findLastDeliveryHouseIndexOnStreet (houseLettersList):
    for index, letters in reversed (list (enumerate (houseLettersList))):
        if (letters != 0):
            return index