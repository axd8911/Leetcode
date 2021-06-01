class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        comb = [(username[i],timestamp[i],website[i]) for i in range(len(username))]
        comb.sort(key=lambda x:x[1])
        dic = collections.defaultdict(list)
        for item in comb:
            dic[item[0]].append(item[2])
        dic = {item:dic[item] for item in dic if len(dic[item])>=3}
        candidates = list(dic.values())
        count = collections.defaultdict(int)
        
        for candidate in candidates:
            user_set = set()
            for i in range(len(candidate)):
                for j in range(i+1,len(candidate)):
                    for k in range(j+1,len(candidate)):
                        user_set.add((candidate[i],candidate[j],candidate[k]))
            for item in user_set:
                count[item]+=1
        length = max(count.values())
        return min([item for item in count if count[item]==length])
