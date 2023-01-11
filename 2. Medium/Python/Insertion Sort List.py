def insertionSortList(head):
    sortedlist = None
        
    while (head != None):
        current      = head
        head         = head.next
        current.next = None
            
        sortedlist = self.insert(sortedlist, current)
        
    return sortedlist
    
def insert(head, new):
    if (head == None):
        return new
    elif (head.val >= new.val):
        new.next = head
        return new
    else:
        pointer = head
        while (pointer.next != None) and (pointer.next.val < new.val):
            pointer = pointer.next
            
        temp         = pointer.next
        pointer.next = new
        new.next     = temp
            
        return head
