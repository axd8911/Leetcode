class Solution:
    def mergeString(self,a,b):
        m,n = 0,0
        output = ''
        while m<len(a) and n<len(b):
            output += a[m]
            output += b[n]
            m+=1
            n+=1
        if m<len(a):
            output += a[m:]
        if n<len(b):
            output += b[n:]
        return output

def main():
    a = 'abcdefg'
    b = 'hijk'
    print (Solution().mergeString(a,b))
main()
