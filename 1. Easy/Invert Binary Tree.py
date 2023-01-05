def invertTree(root, new = 0):
    if not root:
        return None
    
    newroot = TreeNode(root.val)
    newroot.left  = invertTree(root.right)
    newroot.right = invertTree(root.left)
        
    return newroot
