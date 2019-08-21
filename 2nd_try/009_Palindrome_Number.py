class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        mirror = 0
        backup = x

        while x:
            rem = x%10
            x = x//10
            mirror = mirror * 10 + rem

        return mirror == backup
