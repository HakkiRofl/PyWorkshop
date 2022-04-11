import random


library_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
                  [5, 6], [6, 6]]

player_pieces = []
A = True
Status = "none"
while A:
    random.shuffle(library_pieces)
    stock_pieces = library_pieces[0:15]
    pc_pieces = library_pieces[15:21]
    player_pieces = library_pieces[21:27]
    if [5, 5] in pc_pieces or [6, 6] in pc_pieces or [5, 5] in player_pieces or [6, 6] in player_pieces:
        A = False
        if [6, 6] in pc_pieces:
            pc_pieces.remove([6, 6])
            Status = "player"
        elif [6, 6] in player_pieces:
            player_pieces.remove([6, 6])
            Status = "computer"
        elif [5, 5] in player_pieces:
            player_pieces.remove([6, 6])
            Status = "computer"
        elif [5, 5] in pc_pieces:
            pc_pieces.remove([6, 6])
            Status = "computer"
print(f"Stock pieces: {stock_pieces}")
print(f"PC pieces: {pc_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Status: {Status}")