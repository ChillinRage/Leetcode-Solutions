class Solution:
    def reverseKGroup(self, head, k):
        if (k == 1):
            return head
        
        left  = None
        right = head
        i     = 1
        while right:
            if i == k:
                if not left:
                    last = head
                    head = self.reverseFirst(head, k)
                else:
                    last = left.next
                    left.next = self.reverseFirst(left.next, k)
                    
                i = 1
                left  = last
                right = left.next
                
            else:
                right = right.next
                i += 1
        
        return head
        
        
    def reverseFirst(self, head, right): # adapted from my reverse linked list 2: medium
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
            
        self.first = None   # first node of the reversed section
        rest = reverse(head, 1) # remaining list not reversed
        head.next = rest
        
        return self.first
