'''Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
'''
'''
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
'''

import heapq
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        i=0
        res = 0
        max_heap=[]
        min_heap = []
        for j in range (len(nums)):
            heapq.heappush(max_heap,(-nums[j],j))
            heapq.heappush(min_heap,(nums[j],j))
            
            while(-max_heap[0][0] - min_heap[0][0] > limit):
                i+=1
                while max_heap[0][1] < i:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < i:
                    heapq.heappop(min_heap)
            res=max(res,j-i+1)
        return res
        