'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.'''

class Solution(object):
    def sortColors(self, nums):
            maxi = max(nums)
            dic = {}
            for i in range(maxi+1):
                dic[i]=0
            for j in nums:
                dic[j]+=1
            sol = []
            for key in dic:
                for k in range(dic[key]):
                    sol.append(key)
            for l in range(len(nums)):
                nums[l] = sol[l]