class UnionFind:
    def __init__(self):
        self.dic = {}
        
    def find(self, x):
        if x not in self.dic:
            self.dic[x] = x        
        if self.dic[x] != x:
            self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    
    def union(self,x,y):
        self.dic[self.find(x)] = self.find(y)



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        all_uf_dic = collections.defaultdict(UnionFind)
        for account in accounts:
            curr_uf = all_uf_dic[account[0]]
            for i in range(1,len(account)):
                curr_uf.union(account[1], account[i])
        
        root_mapping = collections.defaultdict(list)
        for name in all_uf_dic:
            for key in all_uf_dic[name].dic:
                root_mapping[(name,all_uf_dic[name].find(key))].append(key)
                
        output = [[item[0]] + sorted(root_mapping[item]) for item in root_mapping]
        return output

            
                
        
