def mergeKLists(lists):
    if   len(lists) == 0: return None;
    elif len(lists) == 1: return lists[0];
        
    if (lists[0] == None):
        return mergeKLists(lists[1:])
    elif (lists[1] == None):
        return mergeKLists(lists[0:1] + lists[2:])
        
    head = (lists[0] if lists[0].val <= lists[1].val else lists[1])
    main = head
    sub  = (lists[1] if lists[0].val <= lists[1].val else lists[0])
        
    while (main.next != None) and (sub != None):
        if main.next.val <= sub.val:
            main = main.next
        else:
            temp = main.next
            main.next = sub
            sub = sub.next
            main = main.next
            main.next = temp
                
    if (main.next == None) and (sub != None):
        main.next = sub
            
    lists = [head] + lists[2:]
    return mergeKLists(lists)
