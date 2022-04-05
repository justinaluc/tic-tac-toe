import images


class Board:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.player_1 = None
        self.player_2 = None
        self.fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winner = None

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def set_new_board(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winner = None
        self.greets()

    def switch_player(self, player):
        if player == self.player_1:
            return self.player_2
        return self.player_1

    def ask_the_field(self):
        while True:
            field = input("Choose number of free field (1-9): ")
            if not field.isdigit():
                print("You have to choose a number")
            elif int(field) > 9 or int(field) < 1:
                print("Field out of range.")
            elif int(field) not in self.fields:
                print("This field is already occupied")
            else:
                self.fields.remove(int(field))
                break
        return int(field)

    def update_board(self, field, player):
        if player == self.player_1:
            for row in range(3):
                for i in range(3):
                    if self.board[row][i] == field:
                        self.board[row][i] = 'O'
        else:
            for row in range(3):
                for i in range(3):
                    if self.board[row][i] == field:
                        self.board[row][i] = 'X'
        self.check_winner()
        return self.board

    def check_winner(self):
        # check 3 in row:
        for row in self.board:
            if row[0] == row[1] == row[2]:
                self.winner = row[0]
        # check 3 in column:
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                self.winner = self.board[0][i]
        # check 3 diagonal:
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.board[1][1]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[1][1]
        return self.winner

    def game_over(self):
        if self.winner == 'O':
            self.show_board()
            print(images.winner)
            print(f"GAME OVER! The winner is >>{self.player_1}<<")
        elif self.winner == 'X':
            self.show_board()
            print(images.winner)
            print(f"GAME OVER! The winner is >>{self.player_2}<<")
        elif len(self.fields) == 0:
            self.show_board()
            print(images.game_over)
            print("GAME OVER! No more empty fields.")
        else:
            return False
        play_again = input("Do you want to play again? Y or N: ")
        if play_again in ["y", "Y", "yes", "YES", "Yes"]:
            self.set_new_board()
            return False
        else:
            print(images.bye)
            return True

    def greets(self):
        print("Welcome to simple >>tic tac toe<< game")
        self.player_1 = input("Give me name of PLAYER O: ")
        self.player_2 = input("Give me name of PLAYER X: ")
        while self.player_2 == self.player_1:
            self.player_2 = input("PLAYER 2 has to differ from PLAYER 1... Try again: ")
        print(f"\nHello >>{self.player_1}<< and >>{self.player_2}<<.\nLet's start the battle...!\n")
