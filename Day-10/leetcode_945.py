'''You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.'''

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        moves = 0
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                incmt = nums[i-1]-nums[i]+1
                nums[i]+=incmt
                moves+=incmt
        return moves