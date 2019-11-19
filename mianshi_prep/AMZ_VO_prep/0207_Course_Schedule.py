class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre = collections.defaultdict(list)
        for a,b in prerequisites:
            pre[b].append(a)

        status = [0] * numCourses
        
        def helper(node,res):
            # print (node)
            if status[node] == 1:
                return False
            if status[node] == 2:
                return True
            status[node] = 1
            for item in pre[node]:
                res = res and helper(item,res)
            status[node] = 2
            return res

        for i in range(numCourses):
            if status[i] == 0:
                status[i] == 1
                if not helper(i,True):
                    return False

        return True
