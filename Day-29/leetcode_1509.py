'''
You are given an integer array nums.
In one move, you can choose one element of nums and change it to any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
 
Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
'''

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)<=4):
            return 0
        nums = sorted(nums)
        i = len(nums)
        res = nums[i-4]-nums[0]
        res = min(res,nums[i-3]-nums[1])
        res = min(res,nums[i-2]-nums[2])
        res = min(res,nums[i-1]-nums[3])
        return res
        