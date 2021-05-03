class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = collections.defaultdict(list)
        for item in strs:
            count = [0] * 26
            for letter in item:
                count[ord(letter) - ord('a')] += 1
            grouping[tuple(count)].append(item)
            
        return grouping.values()
                
