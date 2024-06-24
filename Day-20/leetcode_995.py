'''
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
'''
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ln = len(nums)
        isFlipped = [False] * ln
        flip = 0
        pastFlipCount = 0

        for i in range(ln):
            if i >= k and isFlipped[i - k]:
                pastFlipCount -= 1

            if pastFlipCount % 2 == nums[i]:
                if i + k > ln:
                    return -1
                pastFlipCount += 1
                flip += 1
                isFlipped[i] = True

        return flip
                    
        
            
        