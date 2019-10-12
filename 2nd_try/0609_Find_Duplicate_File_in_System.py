class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # split each string based on ' '
        # dictionary: content in () is the key and curr[0] +/+prev is the value. return all values

        paths = [item.split(' ') for item in paths]

        dic = collections.defaultdict(list)

        for item in paths:
            #print (item)
            for i in range(1,len(item)):
                idx1 = item[i].index('(')
                idx2 = len(item[i])-1
                #print (item[i][idx1+1:idx2])
                #print (item[0]+'/'+item[i][:idx1])
                dic[item[i][idx1+1:idx2]].append(item[0]+'/'+item[i][:idx1])

        #print (dic)
        res = []
        for key in dic:
            if len(dic[key]) >1:
                res.append(dic[key])

        return res
