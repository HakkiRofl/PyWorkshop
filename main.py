import random

table = []
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
table.append(start_domino)
B = True
error = ""
while B:
    print("=" * 70)
    print(f"\nStock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(pc_pieces)} \n")
    if len(table) < 7:
        print(*table, "\n")
    elif len(table) >= 7:
        print(*table[0:3],"...", *table[-4:-1], "\n")
    for i, domino in enumerate(player_pieces, start=1):
        print(f"{i}:{domino}")
    if Status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    elif Status == "player":
        print("\nStatus: It's your turn to make a move. Enter your command.")
    print(error)
    error = ""
    try:
        if len(player_pieces) > 0:
            move = int(input())
            if move == 0 :
                player_pieces.append(stock_pieces[0])
                stock_pieces.remove(stock_pieces[0])
            else:
                table.append(player_pieces[move - 1])
                player_pieces.remove(player_pieces[move - 1])
                Status = "computer"
        else:
            print("Status: You WIN!✔✔✔")
            B = False
    except ValueError:
        ai = random.randint(0, len(pc_pieces) - 1)
        if len(pc_pieces) > 1:
            if ai == 0:
                pc_pieces.append(stock_pieces[0])
                stock_pieces.remove(stock_pieces[0])
            else:
                if len(stock_pieces) != 0:
                    table.append(pc_pieces[ai])
                    pc_pieces.remove(pc_pieces[ai])
                    Status = "player"
        else:
            print("Status: Computer WIN!✔✔✔")
            B = False
    except TypeError:
        error = ("Invalid input")
    except IndexError:
        error = ("Invalid input, number > pieces")
