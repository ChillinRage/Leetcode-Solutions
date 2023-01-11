class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode temp = null;
        int sum;
        boolean ten = false;
        
        //add the individual digits (same position) together.
        while (l1 != null && l2 != null) {
            sum = l1.val + l2.val;
            
            if (ten) {
                sum++;
                ten = false;
            }
            
            if (sum >= 10) {
                sum = sum % 10;
                ten = true;
            }
            
            if (head == null) {
                head = new ListNode(sum);
                temp = head;
            } else {
                temp.next = new ListNode(sum);
                temp = temp.next;
            }
            
            l1 = l1.next;
            l2 = l2.next;
        }
        
        //For num1 and num2 with different orders (e.g. 3 and 86)
        ListNode excess = null;
        if (l1 != null) {
            excess = l1;
        } else if (l2 != null) {
            excess = l2;
        }
        
        while (excess != null) {
            if (ten) {
                excess.val++;
                ten = false;
            }
            
            if (excess.val >= 10) {
                ten = true;
                excess.val = excess.val % 10;
            }
            
            temp.next = new ListNode(excess.val);
            temp = temp.next;
            excess = excess.next;
        }
        
        if (ten) {
            temp.next = new ListNode(1);
        }
        
        
        return head;
    } 
}