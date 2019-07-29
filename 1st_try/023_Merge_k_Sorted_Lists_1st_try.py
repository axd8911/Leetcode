'''
Two solutions for this question.
Solution2 is by using linked list approaches. 12%
Solution2 is really sometimes 玄学. I should practise more and master the approach of assigning addresses and avoid affecting other variables. It is a very good example to lean linked list operation. #24 is another good example.

Solution1 is by using list. 61.5%
It is so tricky. We just export all data to a list, do the sorting, and then create another linked list from the sorted list. Crazy!

Others may have faster approaches by using either linked list of list. Check them please!

'''



# Solution 1

class Solution(object):
    def mergeKLists(self, lists):
        
        all_data = []
        
        for item in lists:
            while item:
                all_data.append(item.val)
                item = item.next
        
        all_data.sort()
        
        result1 = result2 = ListNode(0)
        
        for item in all_data:
            result2.next = ListNode(0)
            result2.next.val = item
            result2 = result2.next
        return result1.next





# Solution 2

class Solution(object):
    def mergeKLists(self, lists):
        
        
        current = result = ListNode(0)
        for i in range(len(lists)):
            current = result
            
            while current.next and lists[i]:

                if current.next.val >= lists[i].val:
                    a = current.next
                    b = lists[i].next
                    current.next = lists[i]
                    current.next.next = a
                    lists[i] = b
                current = current.next


                       
            if lists[i]:
                current.next = lists[i]


        return result.next

        
        
