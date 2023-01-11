def addTwoNumbers(l1, l2):
        num1 , num2 = '' , ''
        
        while l1: # iterate first list
            num1 = str(l1.val) + num1
            l1 = l1.next
            
        while l2: # iterate second list
            num2 = str(l2.val) + num2
            l2 = l2.next

        summ = str(int(num1) + int(num2))
        temp = ListNode(int(summ[0]))
        
        for i in summ[1:]: # create node for every digit
            newNode = ListNode(int(i),temp)
            temp    = newNode

        return temp
