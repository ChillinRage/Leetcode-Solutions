def sortList(head):
    if (head == None) or (head.next == None):  # empty or 1 node
        return head
        
        
    pointer = head
    first   = None
    second  = None
    current = 'first'
        
    while (pointer != None):
        temp      = pointer
        pointer   = pointer.next
            
        if (current == 'first'):
            temp.next = first
            first     = temp
            current   = 'second'
        else:
            temp.next = second
            second    = temp
            current   = 'first'
            
    first  = sortList(first)
    second = sortList(second)
        
    return merge(first, second)
    
def merge(first, second):
    if (first == None):
        return second
    elif (second ==  None):
        return first
    else:
        if (first.val <= second.val):
            main = first
            sub  = second
        else:
            main = second
            sub  = first
            
        pointer = main
        
        while (sub != None) and (pointer.next != None):
            if pointer.next.val < sub.val:
                pointer = pointer.next
            else:
                temp = pointer.next
                pointer.next = sub
                sub = sub.next
                pointer = pointer.next
                pointer.next = temp
                
        if (pointer.next == None):
            pointer.next = sub
            
        return main
