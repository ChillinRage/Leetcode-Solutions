def deepestLeavesSum(root):
    def traverse(root, depth):
        nonlocal deep
        nonlocal summ
        
        if root == None:
            return
            
        if depth > self.deep:
            summ  = 0
            deep  = depth
            
        if depth == deep:
            summ += root.val
            
        traverse(root.left,  depth + 1)
        traverse(root.right, depth + 1)
                
    deep   = 0
    summ   = 0
    traverse(root, 0)

    return summ
