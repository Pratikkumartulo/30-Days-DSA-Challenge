'''Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.'''

import math
class Solution(object):
    def judgeSquareSum(self, c):
        ptr = False
        for i in range(0,int(math.sqrt(c))+1):
            j = c - i**2
            if int(math.sqrt(j))**2 == j:
                return True
        return False