# File: tic_tac_toe.py - cli game to learn dev logic and code structure
# import random
from random import randint


class TicTacToe:

    def __init__(self):
        # print('object yay')  # prove that init called on object creation
        self.board = []

    def start_game(self):
        print('\nWelcome! Let\'s Play Tic-Tac-Toe')
        self.create_board()

        # replace fxn call with randint(0,1) to remove fxn
        player = 'X' if self.get_player_one() == 1 else 'O'

        # game loop (no tracking var this time - see hangman for alt.way)
        while True:
            print(f"Player {player}'s turn...")
            self.render_board()

            # take user input
            row, col = list(
                map(int, input("Enter row and column numbers to mark a spot: ").split()))
            # print(f'you picked row {row} and column {col}')

            # mark the spot based on user selection
            self.mark_spot(row - 1, col - 1, player)

            # check for a win # TODO: fix this broken code
            # if self.is_game_won(player):
            #     print(f'Player {player} wins thew game!')
            #     break

            # check for a tie game (all spaces filled) Works!
            if self.is_game_tied():
                print(f'Game Ends in a Draw')
                break

            # next player's turn
            player = self.switch_player_turn(player)

        print()
        self.render_board()

    def create_board(self):
        for i in range(3):
            row = []  # create 3 empty rows
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def render_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def get_player_one(self):
        # print(randint(0, 1))
        return randint(0, 1)

    def mark_spot(self, row, col, player):
        self.board[row][col] = player  # assign 'X' or 'O' to the grid

    def switch_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    # TODO: refactor this ugly code to be more pythonic
    def is_game_won(self, player):
        win = None
        n = len(self.board)
        # checking rows and cols
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
                elif self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
            elif self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        # all 8 winning ways checked w/o success
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_game_tied(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True


# 9- create class instance and start the game (no __main__ deal?)
my_tic_tac_toe = TicTacToe()
my_tic_tac_toe.start_game()
