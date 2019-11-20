class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        combine = []
        for i in range(len(username)):
            combine.append((timestamp[i], username[i], website[i]))
        combine.sort()
        timestamp = [item[0] for item in combine]
        username = [item[1] for item in combine]
        website = [item[2] for item in combine]

        user = collections.defaultdict(list)
        for i in range(len(username)):
            user[username[i]].append(website[i])
        cnt = collections.defaultdict(set)
        for key in user:
            for i in range(len(user[key])):
                for j in range(i+1,len(user[key])):
                    for k in range(j+1,len(user[key])):
                        cnt[(user[key][i],user[key][j],user[key][k])].add(key)

        res = []
        most = 0
        for key in cnt:
            if len(cnt[key])>most:
                most = len(cnt[key])
                res = [key]
            elif len(cnt[key])==most:
                res.append(key)
        res.sort()
        return res[0]
