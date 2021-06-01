class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = collections.defaultdict(int)
        for item in cpdomains:
            count,dns =item.split(' ')
            domain = dns.split('.')
            for i in range(len(domain)):
                dic['.'.join(domain[i:len(domain)])] += int(count)
        return [str(dic[item])+' '+item for item in dic]
            
