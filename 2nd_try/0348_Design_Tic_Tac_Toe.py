class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.col,self.row,self.d,self.di = [],[],[],[]
        # each player should be col info, row info, diag info
        for i in range(2):
            self.col.append([set() for i in range(n)])
            self.row.append([set() for i in range(n)])
            self.d.append(set())
            self.di.append(set())


    def move(self, row: int, col: int, player: int) -> int:

        self.col[player-1][col].add(row)
        self.row[player-1][row].add(col)

        if row==col:
            self.d[player-1].add((col,row))
            if len(self.d[player-1])==self.n:
                return player

        if row + col == self.n - 1:
            self.di[player-1].add((col,row))
            if len(self.di[player-1])==self.n:
                return player

        if len(self.col[player-1][col])==self.n or len(self.row[player-1][row])==self.n:
            return player

        else:
            return 0
