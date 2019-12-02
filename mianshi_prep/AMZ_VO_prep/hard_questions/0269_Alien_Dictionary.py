class Solution:
    def alienOrder(self, words: List[str]) -> str:
        dic = collections.defaultdict(list)
        curr = collections.deque([(0,len(words)-1)])
        order = []

        step = 0
        while curr:
            length = len(curr)
            for i in range(length):
                order.append([])
                l,r = curr.popleft()
                start = l
                for idx in range(l,r+1):
                    if len(words[idx])>step:
                        if idx==l:
                            order[-1].append(words[idx][step])
                        if idx>l and (len(words[idx-1])<=step or words[idx][step] != words[idx-1][step]):
                            order[-1].append(words[idx][step])
                            curr.append((start,idx-1))
                            start = idx
                        if idx==r:
                            curr.append((start,r))
            step += 1

        for item in order:
            for i in range(len(item)):
                dic[item[i]] += item[i+1:]

        status = {key:0 for key in dic.keys()}
        res = []
        def helper(letter,judge):
            if status[letter] == 1:
                return False
            if status[letter] == 2:
                return True
            status[letter] = 1
            for item in dic[letter]:
                judge = judge and helper(item,judge)
            status[letter] = 2
            res.append(letter)
            return judge

        for key in dic.keys():
            if not helper(key,True):
                return ''
        return ''.join(res[::-1])


        
