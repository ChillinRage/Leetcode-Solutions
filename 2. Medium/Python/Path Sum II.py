class Solution:
    
    def pathSum(self, root, targetSum) -> List[List[int]]:
        self.output = []
        self.path = []
        
        return self.output
        
    def traverseToLeaf(self, root, remaining, path):
        # not a node
        if (root == None): return 
        
        path.append(root.val)
        
        # is leaf
        if (root.left == None and root.right == None):
            # path equals target
            if (root.val == remaining):
                # add to output
                self.output.append(path[:])
        else:
            # traverse its children
            self.traverseToLeaf(root.left, remaining - root.val, path)
            self.traverseToLeaf(root.right, remaining - root.val, path)
        
        path.pop() # remove itself after traversing
