#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mehmet Eyüpoğlu
"""

"""
Exercise 24

This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other 
exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look 
like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
 (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to 
the screen using Python’s print statement.

"""
#solution 1
a = '---'.join('    ')
b = '   '.join('||||')

print('\n'.join((a, b, a, b, a, b, a)))

#solution 2
def drawboard(num):
    num = int(num)
    i = 0
    ho = ' ---'
    ve = '|   '
    ho = ho * num
    ve = ve * (num+1)
    
    while i < (num+1):
        print(ho)
        if i != num:
            print(ve)
        i += 1
    
drawboard(3)
