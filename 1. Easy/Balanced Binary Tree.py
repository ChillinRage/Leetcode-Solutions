def isBalanced(root):
    if not root:
        return True
        
    def loop(root, depth=0):
        if not root:
            return depth
        
        depth += 1
        left   = loop(root.left,  depth)
        right  = loop(root.right, depth)
        
        if 0 in [left,right]:
            return 0
        
        if abs(left - right) > 1:
            return 0
        else:
            return max(left,right)
            
    return loop(root)
