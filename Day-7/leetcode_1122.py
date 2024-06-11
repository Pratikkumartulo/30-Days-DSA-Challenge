'''Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.'''

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in sorted(arr1):
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sol = []
        for j in arr2:
            if j in dic:
                sol.extend([j] * dic[j])
                dic[j] = 0
        remelem = []
        for k in dic:
            if dic[k] > 0:
                remelem.extend([k] * dic[k])
        sol.extend(sorted(remelem))
        return sol