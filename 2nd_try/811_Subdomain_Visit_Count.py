class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #separate to count and domain
        sep1 = [item.split(' ') for item in cpdomains]
        sep2 = [item[1].split('.') for item in sep1]

        cnt = collections.defaultdict(int)

        for i in range(len(sep2)):
            for j in range(len(sep2[i])):
                cnt['.'.join(sep2[i][j:])] += int(sep1[i][0])

        return [str(cnt[item])+' '+item for item in cnt]
