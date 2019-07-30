class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.graph = [set() for _ in range(n)]
        for item in edges:
            self.graph[item[0]].add(item[1])
            self.graph[item[1]].add(item[0])

        curr = n//2
        l_curr = self.depth(curr)


        while True:
            smaller = False
            for item in self.graph[curr]:
                l_new = self.depth(item)
                if l_new == l_curr:
                    return [curr,item]
                elif l_new < l_curr:
                    l_curr = l_new
                    curr = item
                    smaller = True
                    break
            if smaller == False:
                return [curr]




    def depth(self,i):

        curr = [i]
        layer = 0
        while curr != []:
            new = []
            for item1 in curr:
                for item2 in self.graph[item1]:
                    if item1 not in self.graph[item2] :
                        new.append(item2)

            layer += 1
            curr = new

        return layer
