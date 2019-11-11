class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        words = []
        nums = []

        for item in logs:
            curr = item.split(' ')
            if curr[1].isalpha():
                words.append(curr)
            else:
                nums.append(item)

        words.sort(key = lambda x : (x[1:], x[0]))
        res = []
        for item in words:
            res.append(' '.join(item))

        return res + nums
