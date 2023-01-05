def hasCycle(head):
    queue = []
    
    while head not in queue:
        queue.append(head)
        if not head:
            break
        
        head = head.next

    return queue[-1]
