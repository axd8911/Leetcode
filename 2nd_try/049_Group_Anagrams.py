class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        
        for item in strs:
            output[tuple(sorted(item))].append(item)

        return output.values()
