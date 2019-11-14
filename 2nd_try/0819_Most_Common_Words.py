class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = list(paragraph)
        banned = set(banned)
        for i in range(len(paragraph)):
            if paragraph[i] in "!?',;.":
                paragraph[i] = ' '
        paragraph = ''.join(paragraph).split(' ')
        paragraph = [item.lower() for item in paragraph if item and item.lower() not in banned]
        cnt = collections.Counter(paragraph)
        maxi = sorted(cnt.values())[-1]
        for key in cnt:
            if cnt[key] == maxi:
                return key
