class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        logs = [item.split(' ') for item in logs]
        word = []
        digit = []
        for item in logs:
            if item[1].isdigit():
                digit.append(item)
            else:
                word.append(item)
        word.sort(key=lambda x:x[1:]+[x[0]])
        word += digit
        word = [' '.join(item) for item in word]

        return word
