class Solution:
    def longestSubstring(self, string, k):
        appear = {}
        left = 0
        longest = 0
        for i, c in enumerate(string):
            appear[c] = i
            if len(appear) > k:
                far = min(appear.values())
                del appear[string[far]]
                left = far+1
            else:
                longest = max(longest, i - left + 1)
        return longest

def main():
    string = 'abbedfcdde'
    k = 7
    result = Solution().longestSubstring(string,k)
    print (result)

main()
