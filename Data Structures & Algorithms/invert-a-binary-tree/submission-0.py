# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        invert = root
        curr = root
        st = [root]
        while curr or st:
            curr = st.pop()
            if curr.left or curr.right:
                tmp = curr.left
                curr.left = curr.right
                curr.right = tmp
            if curr.left:
                st.append(curr.left)
            if curr.right:
                st.append(curr.right)
            curr = None
        return invert


        