import numpy as np
import heapq
from collections import deque

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), ' ')

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for row in self.board:
            if np.all(row == player):
                return True
        for col in self.board.T:
            if np.all(col == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def is_draw(self):
        return np.all(self.board != ' ')

    def get_available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r, c] == ' ']

    def make_move(self, row, col, player):
        if self.board[row, col] == ' ':
            self.board[row, col] = player
            return True
        return False

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
        print("\n")

# **BFS AI Algorithm**
def bfs_ai(game, player):
    queue = deque([(game.board.copy(), player)])

    while queue:
        board_state, current_player = queue.popleft()
        
        for move in game.get_available_moves():
            new_board = board_state.copy()
            new_board[move] = current_player
            
            if game.is_winner(current_player):
                return move  

            queue.append((new_board, 'O' if current_player == 'X' else 'X')) 

    return game.get_available_moves()[0]  # Default to first available move

# **DFS AI Algorithm**
def dfs_ai(game, player):
    stack = [(game.board.copy(), player)]

    while stack:
        board_state, current_player = stack.pop()
        
        for move in game.get_available_moves():
            new_board = board_state.copy()
            new_board[move] = current_player
            
            if game.is_winner(current_player):
                return move  

            stack.append((new_board, 'O' if current_player == 'X' else 'X')) 

    return game.get_available_moves()[0]  # Default to first move

# **Heuristic for A***
def heuristic(board, player):
    """ Simple heuristic: Count potential winning lines for the player """
    score = 0
    for row in board:
        if np.count_nonzero(row == player) == 2 and np.count_nonzero(row == ' ') == 1:
            score += 10
    return score

# **A* AI Algorithm**
def a_star_ai(game, player):
    priority_queue = []
    heapq.heappush(priority_queue, (0, game.board.copy(), player))

    best_move = None
    max_score = float('-inf')

    while priority_queue:
        _, board_state, current_player = heapq.heappop(priority_queue)
        
        for move in game.get_available_moves():
            new_board = board_state.copy()
            new_board[move] = current_player
            score = heuristic(new_board, player)
            
            if score > max_score:
                max_score = score
                best_move = move
            
            next_player = 'O' if current_player == 'X' else 'X'
            heapq.heappush(priority_queue, (score, new_board.copy(), next_player))

    return best_move if best_move else game.get_available_moves()[0]  # Default move

# **Main Game Loop**
def play_game():
    game = TicTacToe()
    game.print_board()

    print("Choose AI Algorithm:")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. A* Search")
    choice = input("Enter your choice (1/2/3): ")

    ai_algorithm = None
    if choice == "1":
        ai_algorithm = bfs_ai
    elif choice == "2":
        ai_algorithm = dfs_ai
    elif choice == "3":
        ai_algorithm = a_star_ai
    else:
        print("Invalid choice. Defaulting to A*.")
        ai_algorithm = a_star_ai

    while not game.is_winner('X') and not game.is_winner('O') and not game.is_draw():
        print("AI is thinking...")
        move = ai_algorithm(game, 'X')  # AI plays as 'X'
        game.make_move(*move, 'X')
        game.print_board()

        if game.is_winner('X'):
            print("AI Wins!")
            break
        elif game.is_draw():
            print("It's a Draw!")
            break

        # **Fix Input Handling**
        while True:
            try:
                player_move = input("Enter your move (row col): ").split()
                if len(player_move) != 2 or not player_move[0].isdigit() or not player_move[1].isdigit():
                    raise ValueError("Invalid input! Enter row and column numbers.")

                row, col = map(int, player_move)
                if game.make_move(row, col, 'O'):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError as e:
                print(e)

        game.print_board()

        if game.is_winner('O'):
            print("You Win!")
            break
        elif game.is_draw():
            print("It's a Draw!")
            break

play_game()