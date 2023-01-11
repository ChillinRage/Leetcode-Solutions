def buildTree(preorder, inorder):
        
    def build(inorder):
        if not inorder:
            return None
            
        root = TreeNode(preorder[0])
        preorder.remove(root.val)
            
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
                    
        root.left  = build(inorder[:i])
        root.right = build(inorder[i+1:])
            
        return root
            
    return build(inorder)
