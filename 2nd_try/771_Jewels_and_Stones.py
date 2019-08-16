class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = collections.Counter(S)

        total = 0

        for item in J:
            if item in cnt:
                total += cnt[item]

        return total
