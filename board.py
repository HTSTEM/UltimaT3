import random

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

    def play_move(self, move, player):
        i, j = move[0], move[1]
        self[i][j] = player
        winner = self.check_win((i,j))
        return winner
        
    def check_win(self,location):
        x,y = location[0],location[1]
        if self[0][y] == self[1][y] == self[2][y]:
            return self[x][y]

        if self[x][0] == self[x][1] == self[x][2]:
            return self[x][y]

        if x == y and self[0][0] == self[1][1] == self[2][2]:
            return self[x][y]

        if x + y == 2 and self[0][2] == self[1][1] == self[2][0]:
            return self[x][y]

        return 0

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
                    if type(self[i][j]) != int:
                        for move in self[i][j].get_legal_moves():
                            legal_moves.append((i,j,move))
        else:
            i, j = self.next_play[0], self.next_play[1]
            moves = self[i][j].get_legal_moves()
            for move in moves:
                legal_moves.append((i, j, move))
        return legal_moves

    def play_move(self, move, player):
        i, j = move[0], move[1]
        x, y = move[2][0], move[2][1]
        sub_board = self[i][j]
        sub_winner = sub_board.play_move(move[2], player)
        winner = 0
        if sub_winner != 0:
            self[i][j] = sub_winner
            winner = self.check_win((i,j))
            
        if type(self[x][y])==int:
            self.next_play=0
        else:
            self.next_play = move[2]
            
        return winner
            
    def check_win(self,location):
        x,y = location[0],location[1]
        if self[0][y] == self[1][y] == self[2][y]:
            return self[x][y]

        if self[x][0] == self[x][1] == self[x][2]:
            return self[x][y]

        if x == y and self[0][0] == self[1][1] == self[2][2]:
            return self[x][y]

        if x + y == 2 and self[0][2] == self[1][1] == self[2][0]:
            return self[x][y]

        return 0

