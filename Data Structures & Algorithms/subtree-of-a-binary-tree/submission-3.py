from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return False
            else:
                return self.isSameTree(node, subRoot) or dfs(node.left) or dfs(node.right)

        return dfs(root)

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        elif (a and not b) or (b and not a):
            return False
        else:
            return a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right) 


if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: subRoot is a subtree
    #     3
    #    / \
    #   4   5
    #  / \
    # 1   2
    root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot1 = TreeNode(4, TreeNode(1), TreeNode(2))
    print(f"Test 1: {sol.isSubtree(root1, subRoot1)}")  # Expected: True
    
    # Test 2: subRoot is NOT a subtree (extra node)
    #     3
    #    / \
    #   4   5
    #  / \
    # 1   2
    #    /
    #   0
    root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subRoot2 = TreeNode(4, TreeNode(1), TreeNode(2))
    print(f"Test 2: {sol.isSubtree(root2, subRoot2)}")  # Expected: False
