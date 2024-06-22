'''Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.'''

'''
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
'''

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        prefix = 0
        result = 0
        countOdd = 0
        for end in range(len(nums)):
            if nums[end]%2!=0:
                countOdd+=1
                prefix = 0
            while countOdd == k:
                prefix +=1
                if nums[start]%2!=0:
                    countOdd-=1
                start+=1
            result+=prefix
        return result
        