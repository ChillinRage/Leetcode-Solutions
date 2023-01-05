def levelOrder(root):
    output = []
    length = -1
        
    def traverse(root, order):
        nonlocal length
        
        if not root:
            return
        else:
            if length < order:
                output.append([])
                length += 1
                    
            output[order].append(root.val)
            traverse(root.left, order + 1)
            traverse(root.right, order + 1)
        
    traverse(root, 0)
    return output
