# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:59:07 2022

@author: lewis
"""

"""
using logs rather than print function
this is so that we don't have to output all unncessary info that are used for 
understanding. If change to true, everything that is logged will be printed as
normal. When false, all we get out is the total distance travelled in the init
"""

logToConsole = False
def log(message):
    if logToConsole:
        print(str(message))


