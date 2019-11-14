class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        exist = {}
        idx = {}
        order = 0
        new = tuple(cells)

        while True:
            exist[new] = order
            idx[order] = new
            order += 1
            cells = new
            new = []

            new.append(0)
            for i in range(1,len(cells)-1):
                if (cells[i-1]==0 and cells[i+1]==0) or (cells[i-1]==1 and cells[i+1]==1):
                    new.append(1)
                else:
                    new.append(0)
            new.append(0)
            new = tuple(new)

            if new in exist:
                break

        if N<order:
            return idx[N]
        return idx[ (N - (exist[new]))%(order-exist[new]) + (exist[new])   ]




            
