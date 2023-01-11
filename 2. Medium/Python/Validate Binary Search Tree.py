class Solution:
    def isValidBST(self, root):
        self.elements = []
        self.inorder(root)
        prev = self.elements[0]
        for each in self.elements[1:]:
            if prev >= each:
                return False
            prev = each
        return True
        
    def inorder(self, node):
        if node == None:
            return
        
        self.inorder(node.left)
        self.elements.append(node.val)
        self.inorder(node.right)
