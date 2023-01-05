def sortedListToBST(head):
    if (not head):
        return None
    elif (not head.next):
        return TreeNode(head.val)
        
    def find_mid(head):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
            
        if length == 1:
            return head
            
        i = 0
        while i < length//2 - 1:
            head = head.next
            i += 1
            
        temp = head.next
        head.next = None
        return temp
        
    tail = find_mid(head)
    root = TreeNode(tail.val)
    tail = tail.next
        
    root.left  = sortedListToBST(head)
    root.right = sortedListToBST(tail)
        
    return root
