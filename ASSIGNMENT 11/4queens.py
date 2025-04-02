import numpy as np

class FourQueensGame:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=int)
        self.current_player = 1  # 1 for AI, -1 for Human

    def is_valid_move(self, row, col):
        if self.board[row][col] != 0:
            return False
        
        for i in range(4):
            if self.board[row][i] != 0 or self.board[i][col] != 0:
                return False
            
            if row - i >= 0 and col - i >= 0 and self.board[row - i][col - i] != 0:
                return False
            if row - i >= 0 and col + i < 4 and self.board[row - i][col + i] != 0:
                return False
            if row + i < 4 and col - i >= 0 and self.board[row + i][col - i] != 0:
                return False
            if row + i < 4 and col + i < 4 and self.board[row + i][col + i] != 0:
                return False
        
        return True
    
    def get_valid_moves(self):
        return [(r, c) for r in range(4) for c in range(4) if self.is_valid_move(r, c)]

    def make_move(self, row, col, player):
        self.board[row][col] = player
    
    def undo_move(self, row, col):
        self.board[row][col] = 0
    
    def is_terminal(self):
        return len(self.get_valid_moves()) == 0
    
    def evaluate(self):
        return np.sum(self.board)  # Simple heuristic: more AI pieces = better
    
    def minimax(self, depth, alpha, beta, maximizing_player):
        if self.is_terminal() or depth == 0:
            return self.evaluate()
        
        if maximizing_player:
            max_eval = -float('inf')
            for move in self.get_valid_moves():
                self.make_move(*move, 1)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.undo_move(*move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_valid_moves():
                self.make_move(*move, -1)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.undo_move(*move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def best_move(self):
        best_val = -float('inf')
        best_move = None
        for move in self.get_valid_moves():
            self.make_move(*move, 1)
            move_val = self.minimax(3, -float('inf'), float('inf'), False)
            self.undo_move(*move)
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move
    
    def play_game(self):
        while not self.is_terminal():
            if self.current_player == 1:
                move = self.best_move()
                if move:
                    self.make_move(*move, 1)
                    print(f"AI placed a queen at {move}")
            else:
                print(self.board)
                move = tuple(map(int, input("Enter row and column (e.g., 1 2): ").split()))
                if self.is_valid_move(*move):
                    self.make_move(*move, -1)
                else:
                    print("Invalid move. Try again.")
                    continue
            self.current_player *= -1
        print("Game over!")
        print(self.board)

if __name__ == "__main__":
    game = FourQueensGame()
    game.play_game()