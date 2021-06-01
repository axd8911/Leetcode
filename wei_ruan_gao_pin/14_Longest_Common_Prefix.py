class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = min([len(item) for item in strs])
        for i in range(length):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[j-1][i]:
                    return strs[j][:i]
        return strs[0][:length]
