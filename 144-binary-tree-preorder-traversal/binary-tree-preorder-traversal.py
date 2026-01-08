# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        result=[]
        # def preorder(node):
        #     if node==None:
        #         return 
        #     result.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        # preorder(root)
        # return result

        stack=[root]
        curr=root
        while len(stack)!=0 :
            curr=stack.pop()
            result.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
