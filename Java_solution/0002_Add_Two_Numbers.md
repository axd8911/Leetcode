```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode res = new ListNode();
        ListNode cal = res;
        int carry = 0;
        int curr;
        
        while (l1 != null || l2 != null || carry != 0){
            
            curr = carry;
            if (l1 != null){
                curr += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                curr += l2.val;
                l2 = l2.next;
            }
            
            cal.next = new ListNode(curr % 10);
            carry = curr / 10;

            cal = cal.next;
        }
        

        
        return res.next;
        
        
    }
}
```