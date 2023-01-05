def partition(head, x):
    before = None
    before_pointer = before
    after = None
    after_pointer = after
    
    while head != None:
        if head.val < x:
            if before == None:
                before = head
                before_pointer = before
            else:
                before_pointer.next = head
                before_pointer = before_pointer.next
        else:
            if after == None:
                after = head
                after_pointer = after
            else:
                after_pointer.next = head
                after_pointer = after_pointer.next
                
        temp = head
        head = head.next
        temp.next = None
        
    if before == None:
         return after
    else:
        before_pointer.next = after
        return before
