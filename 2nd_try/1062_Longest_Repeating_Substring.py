class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:

        start = 0
        end = len(S) - 1

        def checker(length):
            hashSet = set()
            for i in range(len(S)-length+1):
                if hash(S[i:i+length]) in hashSet:
                    return True
                else:
                    hashSet.add(hash(S[i:i+length]))
            return False

        while start<=end:
            mid = (start+end)//2
            if checker(mid) and not checker(mid+1):
                return mid

            if checker(mid):
                start = mid+1
            else:
                end = mid-1




                
