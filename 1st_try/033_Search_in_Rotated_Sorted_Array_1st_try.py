class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums == []:
            return -1
        
        pivot = nums
        cnt = 0
        
        while pivot:
            pos = len(pivot) // 2
            if pivot[pos] > nums[-1]:
                cnt = cnt + len(pivot[:pos+1])
                pivot = pivot[pos+1:]
                
            else:
                pivot = pivot[:pos]       
        p2 = nums
        c2 = 0
        if target <= nums[-1]:
            c2 = c2 + len(p2[:cnt])
            p2 = p2[cnt:]
            
        elif target >= nums[0]:
            p2 = p2[:cnt]
        
        while p2:
            pos = len(p2) // 2
            if p2[pos] == target:
                return c2 + pos
            if p2[pos] > target:
                p2 = p2[:pos]
            elif p2[pos] < target:
                c2 = c2 + len(p2[:pos+1])
                p2 = p2[pos+1:]
               
                
        return -1
                
            
        
