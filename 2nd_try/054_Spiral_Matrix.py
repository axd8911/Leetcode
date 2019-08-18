class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        output = []
        cutter = 0

        while True:
            new = []
            for i in range(cutter,len(matrix[0])-cutter):
                new.append(matrix[cutter][i])
            if not new:
                break
            output.extend(new)

            new = []
            for i in range(cutter+1,len(matrix)-cutter):
                new.append(matrix[i][-1-cutter])
            if not new:
                break
            output.extend(new)
            new = []
            for i in range(len(matrix[0])-2-cutter,-1+cutter,-1):
                new.append(matrix[-1-cutter][i])
            if not new:
                break
            output.extend(new)

            new = []
            for i in range(len(matrix)-2-cutter,cutter,-1):
                new.append(matrix[i][cutter])

            if not new:
                break
            output.extend(new)
            cutter += 1

        return output
