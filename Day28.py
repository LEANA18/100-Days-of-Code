#Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 Example 1:
 **********
              1
            2   3
          4  5  6
Input: root = [1,2,3,4,5,6]
Output: 6
  
Example 2:
*********

Input: root = []
Output: 0
  
Example 3:
**********

Input: root = [1]
Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left,right = root,root
        l,r = 0,0
        while left != None:
            l += 1
            left = left.left
        while right != None:
            r += 1
            right = right.right
        if l == r:
            return (1<<l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
      
Input
****
root = [1,2,3,4,5,6]

Output
*****
6
        

      
   
