class TTT_Board(list):
    
    def __init__(self):
        list.__init__(self,
                      [[0,0,0] for i in range(3)]
        )
        
    def get_legal_moves(self):
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if self[i][j] == 0:
                    legal_moves.append((i,j))
        return legal_moves

class UTTT_Board(list):
    def __init__(self):
        list.__init__(self,
                      [[TTT_Board() for i in range(3)] for i in range(3)]
        )
        self.next_play = 0
        
    def get_legal_moves(self):
        legal_moves=[]
        if self.next_play == 0:
            for i in range(3):
                for j in range(3):
                    for move in self[i][j].get_legal_moves():
                        legal_moves.append((i,j,move))
        else:
            i, j = self.next_play[0], self.next_play[1]
            moves = self[i][j].get_legal_moves()
            for move in moves:
                legal_moves.append((i, j, move))
        return legal_moves
