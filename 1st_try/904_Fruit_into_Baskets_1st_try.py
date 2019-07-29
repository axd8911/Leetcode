'''
Leetcode gives 71.23%, which is almost in the first main range of submissions
Storage usage is 5%. I always use more space than others, should figure out why
The question description is confusing. After making it clear, the main idea is quite straightforward


Comments:
1. may need to consider my accuracy, try to be correct at first, instead of check and doing minor modifications. Minor modifications will make the program more and more complex
2. Should look at other people's solution and see if there is any better thoughts

'''


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # longest in-sequence elements which only contains two 'fruits'
        
        myBusket = []
        allItems = []
        longest = 0
        n = 0
        
        for i in range(0,len(tree)):

            if tree[i] not in myBusket:
                myBusket.append(tree[i])
                n = n + 1
            if n <= 2:
                longest = i + 1

            if len(myBusket) > 2:
                for j in range(len(allItems)-1,-1,-1):
                    if allItems[j] != allItems[j-1]:
                        myBusket.remove(allItems[j-1])
                        del allItems[0:j]
                        break

            allItems.append(tree[i])
            if len(allItems) > longest:
                    longest = len(allItems)
    
        return longest
            
