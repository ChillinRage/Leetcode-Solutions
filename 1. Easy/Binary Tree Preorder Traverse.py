def preorderTraversal(root):
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
