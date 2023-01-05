def postorderTraversal(root):
        if not root:
            return []
        return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]
