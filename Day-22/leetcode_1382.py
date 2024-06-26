'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inordered = []
        def inordertraverse(root):
            if root is None:
                return
            if root.left:
                inordertraverse(root.left)
            inordered.append(root.val)
            if root.right:
                inordertraverse(root.right)
                
        def sortedTree(inordered):
            if not inordered:
                return
            mid = len(inordered)//2
            root = TreeNode(inordered[mid])
            root.left = sortedTree(inordered[:mid])
            root.right = sortedTree(inordered[mid+1:])
            return root
        
        inordertraverse(root)
        return sortedTree(inordered)