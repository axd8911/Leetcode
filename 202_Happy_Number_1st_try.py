class Solution:
    def isHappy(self, n: int) -> bool:
        
        existing = {}
        
        result = n
        
        while result not in existing:
            existing[result] = None
            sumup = 0
            for item in str(result):
                sumup += int(item)**2
            if sumup == 1:
                return True
            else:
                result = sumup
            
            
        return False
            
        
            
