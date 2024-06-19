'''You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.'''

class Solution(object):
    def minDays(self, bloomDay, m, k):
        def canMakeBouque(bloomDay,mid,k):
            boq = 0
            conboq = 0
            for i in bloomDay:
                if i<=mid:
                    conboq+=1
                else:
                    conboq=0
                if conboq==k:
                    boq+=1
                    conboq = 0
            return boq
            
        mindays = -1  
        start = 0
        end = max(bloomDay)
        while start<=end:
            mid = (start+end)//2
            if (canMakeBouque(bloomDay,mid,k)>=m):
                mindays = mid
                end = mid-1
            else:
                start=mid+1
        return mindays
        