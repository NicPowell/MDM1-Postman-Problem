# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:54:29 2022

@author: lewis
"""

""" ----------------------------------------------------------------------------------------------------------

- The beginning of the 'front' of first house on the street is the at the beginning of the street
- The end of the 'front' of last house on the street is the at the end of the street 
- The deliver point of the house (entrance of the property so drive/door etc) is considered to be at the 'end' of the house
  o- The entrance location was considered to have no/little effect
  o- If the house has a drive the walking up and down the drive is constant and should not determine the shortest route
- Lamp posts' are used to represent 'cart lock up points'. This doesn't just need to be lamp posts. 


First model below 'StreetSide A' looks something like.....
:: = door (entrance)
 * = lamp post (lock up point)

               _____________________________________________________________________________________________________________
houseNo....   |    0    |    1     |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |
letters....   |    5    |    5     |    5     |    5     |    5     |    5     |    5     |    5     |    5     |    5     | 
              |        ::         ::         ::         ::         ::         ::         ::         ::         ::         ::
              --------------------------------------------------------------------------------------------------------------
lamp posts..  *                               *                                *                                *

distance      0       10          20         30         40         50         60         70          80        90         100

"""
#  StreetSide A - nice spread all houses
StreetSide_A_LampPosts                               =   [0,       30,         60,         90    ]
StreetSide_A_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_A_HouseLetters                            =   [  5,  5,  5,  5,  5,  5,  5,  5,  5,  5]
StreetSide_A_MaxSackLetters                          =   15

OppositeStreetSide_A_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_A_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_A_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_A_HouseLetters                    =   [  5,  5,  5,  5,  5,  5,  5,  5,  5,  5]
Street_A_Width                                       =   5


# StreetSide B - some no delieveries
StreetSide_B_LampPosts                               =   [ 0,      30,         60,         90    ]
StreetSide_B_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_B_HouseLetters                            =   [  5,  0,  0,  5,  5,  0,  0,  0,  0,  5]
StreetSide_B_MaxSackLetters                          =   15

OppositeStreetSide_B_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_B_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_B_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_B_HouseLetters                    =   [  5,  0,  0,  5,  5,  0,  0,  0,  0,  5]
Street_B_Width                                       =   5


# StreetSide C - first & last house only
StreetSide_C_LampPosts                               =   [ 0,      30,         60,         90    ]
StreetSide_C_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_C_HouseLetters                            =   [  5,  0,  0,  0,  0,  0,  0,  0,  0,  5]
StreetSide_C_MaxSackLetters                          =   15

OppositeStreetSide_C_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_C_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_C_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_C_HouseLetters                    =   [  5,  0,  0,  0,  0,  0,  0,  0,  0,  5]
Street_C_Width                                       =   5

# StreetSide D - last house only
StreetSide_D_LampPosts                               =   [ 0,      30,         60,         90    ]
StreetSide_D_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_D_HouseLetters                            =   [  0,  0,  0,  0,  0,  0,  0,  0,  0,  5]
StreetSide_D_MaxSackLetters                          =   15

OppositeStreetSide_D_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_D_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_D_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_D_HouseLetters                    =   [  0,  0,  0,  0,  0,  0,  0,  0,  0,  5]
Street_D_Width                                       =   5

# StreetSide E - first house only
StreetSide_E_LampPosts                               =   [ 0,      30,         60,         90    ]
StreetSide_E_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_E_HouseLetters                            =   [  5,  0,  0,  0,  0,  0,  0,  0,  0,  0]
StreetSide_E_MaxSackLetters                          =   15

OppositeStreetSide_E_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_E_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_E_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_E_HouseLetters                    =   [  5,  0,  0,  0,  0,  0,  0,  0,  0,  0]
Street_E_Width                                       =   5

# StreetSide F one post
StreetSide_F_LampPosts                               =   [                     60,               ]
StreetSide_F_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_F_HouseLetters                            =   [  5,  0,  5,  0,  5,  0,  5,  0,  5,  0]
StreetSide_F_MaxSackLetters                          =   15

OppositeStreetSide_F_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_F_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_F_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_F_HouseLetters                    =   [  5,  0,  5,  0,  5,  0,  5,  0,  5,  0]
Street_F_Width                                       =   5

#  StreetSide G 
StreetSide_G_LampPosts                               =   [0,       30,         60,         90    ]
StreetSide_G_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_G_HouseLetters                            =   [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
StreetSide_G_MaxSackLetters                          =   15

OppositeStreetSide_G_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_G_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_G_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_G_HouseLetters                    =   [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
Street_G_Width                                       =   5

#  StreetSide H 
StreetSide_H_LampPosts                               =   [0,                 60,                 ]
StreetSide_H_HouseFronts                             =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_H_HouseLetters                            =   [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
StreetSide_H_MaxSackLetters                          =   15

OppositeStreetSide_H_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_H_HouseFronts_DistanceFromStart           =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_H_HouseFronts_DistanceFromStart   =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
OppositeStreetSide_H_HouseLetters                    =   [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
Street_H_Width                                       =   5


#   Street M mixed spread
StreetSide_Z_LampPosts                               =   [0,30,60,90,150,180]
StreetSide_Z_HouseFronts                             =   [ 8,  8,  8,   8,  8,  8,  8,  8,  8,  8, 10, 10, 10, 10, 10, 10, 10, 10, 50, 50]
StreetSide_Z_HouseLetters                            =   [ 2,  5,  4,  47,  0,  0,  0,  0,  0,  0,  4,  8,  9, 12, 45,  6,  4,  7,  6,  60]
StreetSide_Z_MaxSackLetters                          =   60

OppositeStreetSide_Z_LampPosts                       =   [0,       30,         60,         90    ]
StreetSide_Z_HouseFronts_DistanceFromStart           =   [ 8,  16,  24,   32,  40,  48,  56,  64,  72,  80, 90, 100, 110, 120, 130, 140, 150, 160, 210, 260]
OppositeStreetSide_Z_HouseFronts_DistanceFromStart   =   [ 8,  16,  24,   32,  40,  48,  56,  64,  72,  80, 90, 100, 110, 120, 130, 140, 150, 160, 210, 260]
OppositeStreetSide_Z_HouseLetters                    =   [ 2,  5,  4,  47,  0,  0,  0,  0,  0,  0,  4,  8,  9, 12, 45,  6,  4,  7,  6,  60]
Street_Z_Width                                       =   5

#-----------------------------------------------------------------------------
#FOLLOWING STREETS ARE USED IN THE REPORT 

# StreetSide U - Typcial Urban Street
StreetSide_U1_LampPosts                              =   [ 0,      30,         60,         90    ]
StreetSide_U1_HouseFronts                            =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_U1_HouseFronts_DistanceFromStart          =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
StreetSide_U1_HouseLetters                           =   [  5,  0,  0,  2,  4,  0,  0,  3,  0,  1]
StreetSide_U1_MaxSackLetters                         =   15

StreetSide_U2_LampPosts                              =   [ 0,      30,         60,         90    ]
StreetSide_U2_HouseFronts                            =   [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_U2_HouseFronts_DistanceFromStart          =   [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
StreetSide_U2_HouseLetters                           =   [  0,  5,  3,  0,  4,  2,  2,  0,  0,  1]
StreetSide_U2_MaxSackLetters                         =   15

StreetWidth_U                                        =   10 


#Streetside R - Typical Rural street
StreetSide_R1_LampPosts                              =   [0, 50, 70, 130]
StreetSide_R1_HouseFronts                            =   [ 10, 15, 20, 10, 10, 10, 18, 15, 15, 12]
StreetSide_R1_HouseFronts_DistanceFromStart          =   [ 10, 25, 45, 55, 65, 75, 93, 108, 123, 135]
StreetSide_R1_HouseLetters                           =   [ 5, 8, 1, 0, 0, 2, 4, 0, 5, 3]
StreetSide_R1_MaxSackLetters                         =   15

StreetSide_R2_LampPosts                              =   [0, 80]
StreetSide_R2_HouseFronts                            =   [20, 13, 10, 10, 8, 16, 18, 15, 11, 14]
StreetSide_R2_HouseFronts_DistanceFromStart          =   [20, 33, 43, 53, 61, 77, 95, 110, 121, 135]
StreetSide_R2_HouseLetters                           =   [ 0, 0, 0, 1, 1, 2, 4, 6, 0, 3]
StreetSide_R2_MaxSackLetters                         =   15

StreetWidth_R                                        =   15
