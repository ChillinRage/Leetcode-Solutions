def oddEvenList(head):
        if head == None or head.next == None:
            return head
        
        odd    = head      # init odd  list with first node
        even   = head.next # init even list with second node
        p_odd  = odd
        p_even = even
        i      = 3
        head   = head.next.next
        
        while head != None:
            if i % 2 == 0:
                p_even.next = head
                p_even      = head
            else:
                p_odd.next  = head
                p_odd       = head
                
            i   += 1
            head = head.next

        p_odd.next = even
        p_even.next = None
        
        return odd
