class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre = collections.defaultdict(list)
        for a,b in prerequisites:
            pre[b].append(a)

        status = [0] * numCourses
        res = []

        def helper(node,check):
            if status[node] == 1:
                return False
            if status[node] == 2:
                return True
            status[node] = 1
            for item in pre[node]:
                check = check and helper(item,check)
            status[node] = 2
            res.append(node)
            return check

        for i in range(numCourses):
            if status[i] == 0:
                if not helper(i,True):
                    return []
        return res[::-1]
                
