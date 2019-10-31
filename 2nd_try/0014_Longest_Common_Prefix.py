class Trie:
    def __init__(self):
        self.root = {}

    def add(self,string):
        curr = self.root
        for item in string:
            if item not in curr:
                curr[item] = {}
            curr = curr[item]
        curr['END'] = None


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        myTrie = Trie()
        for item1 in strs:
            myTrie.add(item1)

        res = []
        #print (myTrie.root)
        curr = myTrie.root
        while curr:
            if len(curr) == 1 and 'END' not in curr:
                key = list(curr.keys())[0]
                res.append(key)
                curr = curr[key]
            else:
                break
        return ''.join(res)


# string method:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        longest = strs[0]

        for item in strs:
            if not item.startswith(longest):
                new = ''
                for i in range(len(item)):
                    if item[i] == longest[i]:
                        new += item[i]
                    else:
                        break
                longest = new
            if not longest:
                break

        return longest
