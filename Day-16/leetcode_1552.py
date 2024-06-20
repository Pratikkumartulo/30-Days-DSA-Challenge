'''In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.'''

'''Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.'''


class Solution(object):
    def maxDistance(self, position, m):
        
        def canPlaceBall(mid,position,m):
            prev = position[0]
            countBall  = 1
            
            for i in range(1,len(position)):
                curr = position[i]
                if position[i]-prev>=mid:
                    prev = curr
                    countBall+=1
                if countBall==m:
                    break
            return countBall==m
                    
        
        position = sorted(position)
        mini = 1
        maxi = position[-1]-position[0]
        while mini<=maxi:
            mid = (mini+maxi)//2
            if (canPlaceBall(mid,position,m)):
                result = mid
                mini = mid+1
            else:
                maxi = mid-1
        return result
        
        