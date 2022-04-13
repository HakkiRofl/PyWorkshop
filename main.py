import random


library_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
                  [5, 6], [6, 6]]

player_pieces = []
A = True
Status = "none"
start_domino = [0, 0]
while A:
    random.shuffle(library_pieces)
    stock_pieces = library_pieces[0:14]
    pc_pieces = library_pieces[14:21]
    player_pieces = library_pieces[21:28]
    if [5, 5] in pc_pieces or [6, 6] in pc_pieces or [5, 5] in player_pieces or [6, 6] in player_pieces:
        A = False
        if [6, 6] in pc_pieces:
            pc_pieces.remove([6, 6])
            Status = "player"
            start_domino = [6, 6]
        elif [6, 6] in player_pieces:
            player_pieces.remove([6, 6])
            Status = "computer"
            start_domino = [6, 6]
        elif [5, 5] in player_pieces:
            player_pieces.remove([5, 5])
            Status = "computer"
            start_domino = [5, 5]
        elif [5, 5] in pc_pieces:
            pc_pieces.remove([5, 5])
            Status = "computer"
            start_domino = [5, 5]
#print(f"Stock pieces: {stock_pieces}")
#print(f"PC pieces: {pc_pieces}")
#print(f"Player pieces: {player_pieces}")
#print(f"Status: {Status}")
print(f"\nThe {Status} makes the first move (status = '{Status}')\n")
print("=" * 70)
print(f"\nStock size: {len(stock_pieces)}")
print(f"Computer pieces: {len(pc_pieces)} \n")
print(start_domino, "\n")
for i, domino in enumerate(player_pieces, start=1):
    print(f"{i}:{domino}")
if Status == "computer":
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
elif Status == "player":
    print("\nStatus: It's your turn to make a move. Enter your command.")