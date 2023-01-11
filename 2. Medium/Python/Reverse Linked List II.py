class Solution:
    def reverseBetween(self, head, left, right):
        def reverse(current, i):
            if (i + 1) == right: # next node is last node to be reversed
                self.first = current.next
                rest = current.next.next
                self.first.next = current
                
                return rest
            else:
                rest = reverse(current.next, i + 1)
                current.next.next = current
                
                return rest
            
        if left == right:
            return head
            
        self.first  = None   # first node of the reversed section
        self.anchor = head  # last node of the front normal section
        
        for _ in range(1, left - 1):
            self.anchor = self.anchor.next
        
        if left == 1:
            rest = reverse(self.anchor, left) # remaining list not reversed
            self.anchor.next = rest
            
            return self.first
        else:
            rest = reverse(self.anchor, left - 1) # remaining list not reversed
            last = self.anchor.next
            last.next = rest
            self.anchor.next = self.first
            
            return head
