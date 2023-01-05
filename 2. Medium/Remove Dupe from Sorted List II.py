def deleteDuplicates(head):
    if head == None:
        return head
        
    current = head
    output  = None
    pointer = None
    status  = True
        
    while current.next != None:
        if current.val == current.next.val:
            status  = False
            current = current.next
        else:
            if status:
                if output == None:
                    output = current
                else:
                    pointer.next = current
                pointer = current
                current = current.next
                pointer.next = None
            else:
                current = current.next
                    
            status = True
        
    if status:
        if output == None:
            output = current
        else:
            pointer.next = current
        
    return output
