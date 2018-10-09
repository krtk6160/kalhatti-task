# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def traverse(self, root, Sum, path, pathArr):
        if not root:
            return
        Sum -= root.val
        if Sum == 0 and not root.left and not root.right:
            pathArr.append(path + [root.val])
            return
        else:
                self.traverse(root.left, Sum, path + [root.val], pathArr)
                self.traverse(root.right, Sum, path + [root.val], pathArr)
        
    def pathSum(self, A, B):
        if not A:
            return []
        path = []
        pathArr = []
        self.traverse(A, B, path, pathArr)
        return pathArr