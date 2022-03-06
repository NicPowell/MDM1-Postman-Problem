from SideOfStreetModels import *
from SingleStreetSideNearestLampPost import *
from SingleStreetSideNextLampPost import *
from PolygonsAcrossTwoSidesOfRoad import *

WalkingSpeed = 2

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#URBAN STREET TO USE IN REPORT

#First algorithm
distanceU1 = singleSideStreetDeliveryNextLampPost(StreetSide_U1_MaxSackLetters,StreetSide_U1_LampPosts,StreetSide_U1_HouseFronts,StreetSide_U1_HouseLetters)
assert distanceU1 == 200, "StreetSideU1 failed"
print("street side U1 with next lamp post algorithm distance is: " + str(distanceU1))

distanceU2 = singleSideStreetDeliveryNextLampPost(StreetSide_U2_MaxSackLetters,StreetSide_U2_LampPosts,StreetSide_U2_HouseFronts,StreetSide_U2_HouseLetters)
assert distanceU2 == 220, "StreetSideU1 failed"
print("street side U2 with next lamp post algorithm distance is: " + str(distanceU2))

UrbanStreetTotalDistanceNextLampPost = distanceU1 + distanceU2 + StreetWidth_U
print("Total distance to deliver to this urban street example using next lamppost algorithm is: " + str(UrbanStreetTotalDistanceNextLampPost) + "m")
UrbanStreetTotalTimeNextLampPost = UrbanStreetTotalDistanceNextLampPost / WalkingSpeed
print("Total time to deliver to this urban street example using the next lamppost algorithm is: " + str(UrbanStreetTotalTimeNextLampPost) + "s")


#Second algorithm
distanceU1 = singleSideStreetDeliveryNearestLampPost(StreetSide_U1_MaxSackLetters,StreetSide_U1_LampPosts,StreetSide_U1_HouseFronts,StreetSide_U1_HouseLetters)
assert distanceU1 == 200, "StreetSideU1 failed"
print("\n" + "street side U1 with nearest lamp post algorithm distance is: " + str(distanceU1))

distanceU2 = singleSideStreetDeliveryNearestLampPost(StreetSide_U2_MaxSackLetters,StreetSide_U2_LampPosts,StreetSide_U2_HouseFronts,StreetSide_U2_HouseLetters)
assert distanceU2 == 180, "StreetSideU2 failed"
print("street side U2 with nearest lamp post algorithm distance is: " + str(distanceU2))

UrbanStreetTotalDistanceNearestLampPost = distanceU1 + distanceU2 + StreetWidth_U
print("Total distance to deliver to this urban street example using nearest lamppost algorithm is: " + str(UrbanStreetTotalDistanceNearestLampPost) + "m")
UrbanStreetTotalTimeNearestLampPost = UrbanStreetTotalDistanceNearestLampPost / WalkingSpeed
print("Total time to deliver to this urban street example using the nearest lamppost algorithm is: " + str(UrbanStreetTotalTimeNearestLampPost) + "s")


#Third algorithm
UrbanStreetTotalDistancePolygonsAcrossTwoSidesOfRoad = PolygonsAcrossTwoSidesOfRoad(StreetSide_U1_LampPosts, StreetSide_U2_LampPosts, StreetSide_U1_HouseFronts_DistanceFromStart, StreetSide_U2_HouseFronts_DistanceFromStart, StreetSide_U1_HouseLetters, StreetSide_U2_HouseLetters, StreetWidth_U, StreetSide_U1_MaxSackLetters)
print("\n" + "Total distance to deliver to this urban street example using the 'polygons across two sides of road' algorithm is: " + str(UrbanStreetTotalDistancePolygonsAcrossTwoSidesOfRoad) + "m")
UrbanStreetTotalTimePolygonsAcrossTwoSidesOfRoad = UrbanStreetTotalDistancePolygonsAcrossTwoSidesOfRoad / WalkingSpeed
print("Total time to deliver to this urban street example using the 'polygons across two sides of road' algorithm is: " + str(UrbanStreetTotalTimePolygonsAcrossTwoSidesOfRoad) + "s")


#Find optimal algorithm:
optimalTime = min(UrbanStreetTotalTimeNextLampPost, UrbanStreetTotalTimeNearestLampPost, UrbanStreetTotalTimePolygonsAcrossTwoSidesOfRoad)

if optimalTime == UrbanStreetTotalTimeNextLampPost:
    print(f'\nThe optimal algorithm for this urban street is the \'next lamppost\' algorithm, with a time of {optimalTime} seconds.')
    
elif optimalTime == UrbanStreetTotalTimeNearestLampPost:
    print(f'\nThe optimal algorithm for this urban street is the \'nearest lamppost\' algorithm, with a time of {optimalTime} seconds.')
    
else:
    print(f'\nThe optimal algorithm for this urban street is the \'polygons across two sides of road\' algorithm, with a time of {optimalTime} seconds.')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#RURAL STREET TO USE IN REPORT 

#First algorithm
distanceR1 = singleSideStreetDeliveryNextLampPost(StreetSide_R1_MaxSackLetters,StreetSide_R1_LampPosts,StreetSide_R1_HouseFronts,StreetSide_R1_HouseLetters)
assert distanceR1 == 355, "StreetSideR1 failed"
print("\n" + "street side R1 with next lamp post algorithm distance is: " + str(distanceR1))

distanceR2 = singleSideStreetDeliveryNextLampPost(StreetSide_R2_MaxSackLetters,StreetSide_R2_LampPosts,StreetSide_R2_HouseFronts,StreetSide_R2_HouseLetters)
assert distanceR2 == 381, "StreetSideR2 failed"
print("street side R2 with next lamp post algorithm distance is: " + str(distanceR2))

RuralStreetTotalDistanceNextLampPost = distanceR1 + distanceR2 + StreetWidth_R
print("Total distance to deliver to this rural street example using next lamppost algorithm is: " + str(RuralStreetTotalDistanceNextLampPost) + "m")
RuralStreetTotalTimeNextLampPost = RuralStreetTotalDistanceNextLampPost / WalkingSpeed
print("Total time to deliver to this rural street example using the next lamppost algorithm is: " + str(RuralStreetTotalTimeNextLampPost) + "s")


#Second algorithm
distanceR1 = singleSideStreetDeliveryNearestLampPost(StreetSide_R1_MaxSackLetters,StreetSide_R1_LampPosts,StreetSide_R1_HouseFronts,StreetSide_R1_HouseLetters)
assert distanceR1 == 265, "StreetSideR1 failed"
print("\n" + "street side R1 with nearest lamp post algorithm distance is: " + str(distanceR1))

distanceR2 = singleSideStreetDeliveryNearestLampPost(StreetSide_R2_MaxSackLetters,StreetSide_R2_LampPosts,StreetSide_R2_HouseFronts,StreetSide_R2_HouseLetters)
assert distanceR2 == 359, "StreetSideR2 failed"
print("street side R2 with nearest lamp post algorithm distance is: " + str(distanceR2))

RuralStreetTotalDistanceNearestLampPost = distanceR1 + distanceR2 + StreetWidth_R
print("Total distance to deliver to this rural street example using nearest lamppost algorithm is: " + str(RuralStreetTotalDistanceNearestLampPost) + "m")
RuralStreetTotalTimeNearestLampPost = RuralStreetTotalDistanceNearestLampPost / WalkingSpeed
print("Total time to deliver to this rural street example using the nearest lamppost algorithm is: " + str(RuralStreetTotalTimeNearestLampPost) + "s")


#Third algorithm
RuralStreetTotalDistancePolygonsAcrossTwoSidesOfRoad = PolygonsAcrossTwoSidesOfRoad(StreetSide_R1_LampPosts, StreetSide_R2_LampPosts, StreetSide_R1_HouseFronts_DistanceFromStart, StreetSide_R2_HouseFronts_DistanceFromStart, StreetSide_R1_HouseLetters, StreetSide_R2_HouseLetters, StreetWidth_R, StreetSide_R1_MaxSackLetters)
print("\n" + "Total distance to deliver to this rural street example using the 'polygons across two sides of road' algorithm is: " + str(UrbanStreetTotalDistancePolygonsAcrossTwoSidesOfRoad) + "m")
RuralStreetTotalTimePolygonsAcrossTwoSidesOfRoad = RuralStreetTotalDistancePolygonsAcrossTwoSidesOfRoad / WalkingSpeed
print("Total time to deliver to this rural street example using the 'polygons across two sides of road' algorithm is: " + str(RuralStreetTotalTimePolygonsAcrossTwoSidesOfRoad) + "s")


#Find optimal algorithm:
optimalTime = min(RuralStreetTotalTimeNextLampPost, RuralStreetTotalTimeNearestLampPost, RuralStreetTotalTimePolygonsAcrossTwoSidesOfRoad)

if optimalTime == RuralStreetTotalTimeNextLampPost:
    print(f'\nThe optimal algorithm for this rural street is the \'next lamppost\' algorithm, with a time of {optimalTime} seconds.')
    
elif optimalTime == RuralStreetTotalTimeNearestLampPost:
    print(f'\nThe optimal algorithm for this rural street is the \'nearest lamppost\' algorithm, with a time of {optimalTime} seconds.')
    
else:
    print(f'\nThe optimal algorithm for this rural street is the \'polygons across two sides of road\' algorithm, with a time of {optimalTime} seconds.')



"""
-------------------------------------------------------------------------------

# StreetSide_A
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->10                       10                move to delivery          10
# -->0 -->10 -->10            30                deliveries                30
# <-- 30                       0                back to cart              60
# -->30                       30                move cart                 90
# -->10                       40                to next house            100
# -->0 -->10 -->10            60                deliveries               120
# <--30                       30                back to cart             150
# -->30                       60                move cart                180
# -->10                       70                to next delivery         190
# -->0 -->10 -->10            90                delivery                 210
# <--30                       90                back to cart             240
# -->30                       90                move cart                270
# -->10                      100                delivery                 280
# <--10                       90                back to cart             290
# -->10                      100                end of street            300
#  Total 300
distance = singleSideStreetDeliveryNextLampPost(StreetSide_A_MaxSackLetters,StreetSide_A_LampPosts,StreetSide_A_HouseFronts,StreetSide_A_HouseLetters)
assert distance == 300, "StreetSideA failed"
print("street side A with next lamp post algorithm distance is: " + str(distance))

# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->0                         0                move to post               0
# -->10                       10                move to delivery          10
# -->0                        10                deliveries                10
# <--10                        0                back to cart              20
# -->30                       30                move cart                 50
# <--10                       20                to next house             60
# -->0 -->10 -->10            40                deliveries                80
# <--10                       30                back to cart              90
# -->30                       60                move cart                120
# <--10                       50                to next delivery         130
# -->0 -->10 -->10            70                delivery                 150
# <--10                       60                back to cart             160
# -->30                       90                move cart                190
# <--10                       80                to next delivery         200
# -->0 -->10 -->10           100                delivery                 220
# <--10                       90                back to cart             230
# -->10                      100                end of street            240
#  Total 240
distance = singleSideStreetDeliveryNearestLampPost(StreetSide_A_MaxSackLetters,StreetSide_A_LampPosts,StreetSide_A_HouseFronts,StreetSide_A_HouseLetters)
assert distance == 240, "StreetSideA failed"
print("street side A with nearest lamp post algorithm distance is: " + str(distance))


# StreetSide_B
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->10                       10                move to delivery          10
# -->0                        10                deliveries                10
# <--10                        0                back to cart              20
# -->30                       30                move cart                 50
# -->10                       40                to next house             60
# -->0 -->10                  50                deliveries                70
# <--20                       30                back to cart              90
# -->60                       90                move cart                150
# -->10                      100                delivery                 160
# <--10                       90                back to cart             170
# -->10                      100                end of street            180
#  Total 180
distance = singleSideStreetDeliveryNextLampPost(StreetSide_B_MaxSackLetters,StreetSide_B_LampPosts,StreetSide_B_HouseFronts,StreetSide_B_HouseLetters)
assert distance == 180, "StreetSide_B failed"
print("street side B with next lamp post algorithm distance is: " + str(distance))

#create an expected model for street B using nearest lamp post model
distance = singleSideStreetDeliveryNearestLampPost(StreetSide_B_MaxSackLetters,StreetSide_B_LampPosts,StreetSide_B_HouseFronts,StreetSide_B_HouseLetters)
assert distance == 180, "StreetSideB failed"
print("street side B with nearest lamp post algorithm distance is: " + str(distance))

# StreetSide_C
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->10                       10                move to delivery          10
# -->0                        10                deliveries                10
# <--10                        0                back to cart              20
# -->90                       90                move cart                110
# -->0                        90                to start next house      110
# -->10                      100                deliveries               120
# <--10                       90                back to cart             130
# -->10                      100                end of street            140
#  Total 140
distance = singleSideStreetDeliveryNextLampPost(StreetSide_C_MaxSackLetters,StreetSide_C_LampPosts,StreetSide_C_HouseFronts,StreetSide_C_HouseLetters)
assert distance == 140, "StreetSide_C failed"
print("street side C with next lamp post algorithm distance is: " + str(distance))

# StreetSide_D
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->90                       90                move cart                 90
# -->10                      100                to next house             90
# -->0                       100                deliveries               100
# <--10                       90                back to cart             110
# -->10                      100                end of street            120
#  Total 120
distance = singleSideStreetDeliveryNextLampPost(StreetSide_D_MaxSackLetters,StreetSide_D_LampPosts,StreetSide_D_HouseFronts,StreetSide_D_HouseLetters)
assert distance == 120, "StreetSide_D failed"
print("street side D with next lamp post algorithm distance is: " + str(distance))

# StreetSide_E
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->10                       10                move to delivery          10
# -->00                       10                deliveries                10
# <--10                        0                back to cart              20
# -->100                     100                end of street            120
#  Total 120
distance = singleSideStreetDeliveryNextLampPost(StreetSide_E_MaxSackLetters,StreetSide_E_LampPosts,StreetSide_E_HouseFronts,StreetSide_E_HouseLetters)
assert distance == 120, "StreetSide_E failed"
print("street side E with next lamp post algorithm distance is: " + str(distance))

# StreetSide_F
# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->60                       60                move cart                 60
# <--50                        0                move to deliver          110
# -->0-->20-->20              50                deliveries               150
# -->10                       60                back to cart             160
# -->0                        60                move to house            160
# -->10-->20                  90                deliveries               190
# <--30                       60                back to cart             220
# -->40                      100                end of street            260
#  Total 280
distance = singleSideStreetDeliveryNextLampPost(StreetSide_F_MaxSackLetters,StreetSide_F_LampPosts,StreetSide_F_HouseFronts,StreetSide_F_HouseLetters)
assert distance == 260, "StreetSide_F failed"
print("street side F with next lamp post algorithm distance is: " + str(distance))

#StreetSide_G

#do expected for street G using the next lamp post model
distance = singleSideStreetDeliveryNextLampPost(StreetSide_G_MaxSackLetters,StreetSide_G_LampPosts,StreetSide_G_HouseFronts,StreetSide_G_HouseLetters)
assert distance == 240, "StreetSide_G failed"
print("street side G with next lamp post algorithm distance is: " + str(distance))


# ____________________________________________________________________________________
# _________________________EXPECTED __________________________________________________
# ___movement___      __street position__       __action___        ___total distance___
# -->0                         0                move to post               0
# -->10                       10                move to delivery          10
# -->0                        10                deliveries                10
# <--10                        0                back to cart              20
# -->30                       30                move cart                 50
# <--10                       20                to next house             60
# -->0                        20                deliveries                60
# -->10                       30                back to cart              70
# <--0                        30                to next house             80
# -->0 -->10                  40                deliveries                80
# <--10                       30                back to cart              90
# -->30                       60                move cart                120
# <--10                       50                to next delivery         130
# -->0                        50                delivery                 130
# -->10 -->10                 70                to next houses           150
# -->0                        70                delivery                 150
# <--10                       60                back to cart             160
# -->30                       90                move cart                190
# <--10                       80                to next house            200
# -->0                        80                deliver                  200
# -->10 -->10                100                to next houses           220
# -->0                       100                deliver                  220
# <--10                       90                back to cart             230
# -->10                      100                to end of road           240
#  Total 240

distance = singleSideStreetDeliveryNearestLampPost(StreetSide_G_MaxSackLetters,StreetSide_G_LampPosts,StreetSide_G_HouseFronts,StreetSide_G_HouseLetters)
assert distance == 240, "StreetSideG failed"
print("street side G with nearest lamp post algorithm distance is: " + str(distance))
"""

