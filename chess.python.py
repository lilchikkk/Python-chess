import copy

class ChessBoard:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'white'  # 'white' or 'black'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, start, end):
        # proverka na validnost' hoda (prosto proverka na pustuyu kletku ili na protivnika)e3
        piece = self.board[start[0]][start[1]]
        target = self.board[end[0]][end[1]]
        if target == '.' or (piece.isupper() and target.islower()) or (piece.islower() and target.isupper()):
            return True
        return False

    def make_move(self, start, end):
        if self.is_valid_move(start, end):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = '.'
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            return True
        return False

def main():
    board = ChessBoard()
    while True:
        board.print_board()
        print(f"Ход {board.current_player}")
        move = input("Введите ход (например, e2 e4): ").split()
        if len(move) != 2:
            continue
        start = (8 - int(move[0][1]), ord(move[0][0]) - ord('a'))
        end = (8 - int(move[1][1]), ord(move[1][0]) - ord('a'))
        if board.make_move(start, end):
            print("Ход сделан")
        else:
            print("Неверный ход")

if __name__ == "__main__":
    main()
