def removeNthFromEnd(head, n):
    history = [head]
    cur = head.next
        
    while cur:
        history.append(cur)
        cur = cur.next
            
    if n == len(history):
        head = head.next
    else:
        prev = history[-1*n - 1]
        cur = history[-1*n].next
        prev.next = cur
            
    return head
