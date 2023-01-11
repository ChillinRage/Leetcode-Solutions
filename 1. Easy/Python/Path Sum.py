def hasPathSum(root, target, summ = 0):
    if not root:
        return False
            
    summ += root.val
    leftsum  = hasPathSum(root.left,  target, summ)
    rightsum = hasPathSum(root.right, target, summ)

    if (not root.left) and (not root.right):
        return summ == target
    
    return (True in [leftsum, rightsum])
