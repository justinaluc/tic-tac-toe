from board import Board
import images

game_over = False
board = Board()
print(images.tic_tac_toe)
board.greets()
player = board.player_1

while not game_over:
    board.show_board()
    print(f"\nNow >>{player}<< is playing")
    field = board.ask_the_field()
    board.update_board(field, player)
    player = board.switch_player(player)
    game_over = board.game_over()
