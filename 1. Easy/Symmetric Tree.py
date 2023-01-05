def isSymmetric(root):
    return Ltraverse(root.left) == Rtraverse(root.right)
        
def Ltraverse(root):
    if not root:
        return 'N'
    return  str(root.val) + Ltraverse(root.left) + Ltraverse(root.right)
    
def Rtraverse(root):
    if not root:
        return 'N'
    return  str(root.val) + Rtraverse(root.right) + Rtraverse(root.left)
