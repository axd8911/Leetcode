class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dic = collections.defaultdict(list)
        for a,b in prerequisites:
            dic[b].append(a)
        
        status = [0] * numCourses
        res = []
        
        def helper(course,judge):
            if status[course]==1:
                return False
            if status[course]==2:
                return True
            status[course]=1
            for item in dic[course]:
                judge = helper(item,judge)
                if judge == False:
                    break
            status[course]=2
            res.append(course)
            return judge
        
        for i in range (numCourses):
            if not helper(i,True):
                return False
        return True
