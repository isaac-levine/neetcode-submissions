class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        # for a node to be good, it must be > the max between the root and it
    

        numGoodNodes = 0 

        def dfs(node, maxVal):
            nonlocal numGoodNodes

            if not node:
                return
            
            if node.val >= maxVal:
                numGoodNodes += 1 
            
            maxVal = max(maxVal, node.val)  
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return numGoodNodes 
