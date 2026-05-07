class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, the structural paths match perfectly
        if not p and not q:
            return True
            
        # If only one node is null, or structural values differ, they are not identical
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check the structural symmetry of left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
