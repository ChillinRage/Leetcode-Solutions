class Solution:
    def recoverFromPreorder(self, string, depth = 0):
        def next_node(string):
            while (string[0] == '-'):                    # remove current node dashes
                string = string[1:]
            while (string != '') and (string[0] != '-'): # remove current node value
                string = string[1:]
            return string
        
        def get_depth():
            depth = 0
            for each in self.string:
                if each != '-':
                    return depth
                else:
                    depth += 1
        def get_val():
            num = False
            val = ''
            for each in self.string:
                if each != '-':
                    num = True
                    val += each
                elif num:
                    return int(val)
                
            return int(val)
        
        self.string = string
        if (string == '') or (get_depth() < depth):  #empty tree or depth of node is lower than current depth
            return None
        
        root = TreeNode(get_val())
        self.string = next_node(string)
        root.left  = self.recoverFromPreorder(self.string, depth + 1)
        root.right = self.recoverFromPreorder(self.string, depth + 1)
        return root
