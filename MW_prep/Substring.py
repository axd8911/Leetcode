class Solution:
    def substring(self,s):
        vowels = {'a','e','i','o','u'}
        combine = []
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] in vowels and s[j] not in vowels:
                    combine.append(s[i:j+1])
        combine.sort()
        return combine[0],combine[-1]

def main():
    s = 'aab'
    print (Solution().substring(s))
main()
