class Solution:
    def swapList(self,s):
        l = 0
        r = len(s)-1
        total = 0
        while l < r:
            num1 = s[l]
            num2 = s[r]
            if num1%2==1:
                l+=1
                continue
            if num2%2==0:
                r-=1
                continue
            print(s)
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
            total +=1
        return total,s

def main():
    s = [1,2,6,3,4,3,3,8,6]
    print (Solution().swapList(s))
main()
