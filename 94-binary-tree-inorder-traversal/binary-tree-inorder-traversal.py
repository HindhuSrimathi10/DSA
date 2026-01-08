# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

    # using recursion
        # def inorder(node):
        #     if node==None:
        #         return 
        #     inorder(node.left)
        #     result.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return result

    # using stack
        stack=[]
        curr=root
        while curr or len(stack)!=0:
            while curr!=None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        return result

