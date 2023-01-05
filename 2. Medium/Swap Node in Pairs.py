def swapPairs(head):
    if not head or not head.next:
        return head
    
    newhead = head.next
    temp = head.next.next
    head.next.next = head
    head.next = swapPairs(temp)

    return newhead
