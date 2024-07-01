'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''

'''
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
'''
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i=0
        j=i+2
        while(j<len(arr)):
            count=0
            for k in range(i,j+1):
                if(arr[k]%2!=0):
                    count+=1
            if count==3:
                return True
            i+=1
            j=i+2
        return False