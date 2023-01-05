class Solution:
    def getMinimumDifference(self, root):
        self.elements = []
        self.inorder(root)
        minm = 10**7
        for i in range(len(self.elements)-1):
            minm = min(minm, self.elements[i+1] - self.elements[i])
        
        return minm
    
    def inorder(self, node):
        if node == None:
            return
        
        self.inorder(node.left)
        self.elements.append(node.val)
        self.inorder(node.right)
