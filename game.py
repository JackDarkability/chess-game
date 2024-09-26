from board import board
from pieces import pawn,knight,rook,king,queen,bishop


def initialise_game():
    # Images are placeholders

    # Black Pieces
    b_r_1 = rook("b",0,7,"black_rook.png")
    b_r_2 = rook("b",7,7,"black_rook.png")

    b_n_1 = knight("b",1,7,"black_knight.png")
    b_n_2 = knight("b",6,7,"black_knight.png")

    b_b_1 = bishop("b",2,7,"black_bishop.png")
    b_b_2 = bishop("b",5,7,"black_bishop.png")

    b_q = queen("b",3,7,"black_queen.png")
    b_k = king("b",4,7,"black_king.png")


    # White Pieces
    w_r_1 = rook("w",0,0,"white_rook.png")
    w_r_2 = rook("w",7,0,"white_rook.png")

    w_n_1 = knight("w",1,0,"white_knight.png")
    w_n_2 = knight("w",6,0,"white_knight.png")

    w_b_1 = bishop("w",2,0,"white_bishop.png")
    w_b_2 = bishop("w",5,0,"white_bishop.png")

    w_q = queen("w",3,0,"white_queen.png")
    w_k = king("w",4,0,"white_king.png")

    
    b_pawns = [pawn("b", i, 6, "black_pawn.png") for i in range(8)]
    w_pawns = [pawn("w", i, 1, "white_pawn.png") for i in range(8)]

    starting_board = [
    [b_r_1,b_n_1,b_b_1,b_q,b_k,b_b_2,b_n_2,b_r_2], 
     b_pawns, 
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    w_pawns,
    [w_r_1,w_n_1,w_b_1,w_q,w_k,w_b_2,w_n_2,w_r_2] 
    ]
    
    return board(starting_board)

starting_board = initialise_game()
print(starting_board.layout[0][1].get_possible_moves(starting_board))