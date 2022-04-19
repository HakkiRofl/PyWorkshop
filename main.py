import random

table = []
library_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
                  [5, 6], [6, 6]]

player_pieces = []
A = True
Status = "none"
start_domino = [0, 0]
level = int(input("Easy - 1, Medium - 2, Hard - 3  : "))
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
active = 0
while B:
    bestvar = []
    if level == 2:
        if active == 1:
            active = 0
        elif active == 0:
            active = 1
    if level == 3 or active == 1:
        text_list = pc_pieces + table
        text1 = [i[0] for i in text_list]
        text2 = [i[1] for i in text_list]
        text_list = text1 + text2
        from collections import defaultdict
        freq_dict = defaultdict(int)
        for word in text_list:
            freq_dict[word] += 1
        for i in pc_pieces:
            bestvar.append(freq_dict[i[0]] + freq_dict[i[1]])
        new_pc_pieces = []
        for i in range(len(pc_pieces)):
            g = 0
            for h in range(len(pc_pieces)):
                if bestvar[h] > g:
                    g = bestvar[h]
                    piec = h
            new_pc_pieces.append(pc_pieces[piec])
            pc_pieces.remove(pc_pieces[piec])
            bestvar.remove(bestvar[piec])
        pc_pieces = new_pc_pieces
    print("=" * 70)
    print(f"\nStock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(pc_pieces)} \n")
    if len(table) < 7:
        print(*table, "\n")
    elif len(table) >= 7:
        print(*table[0:3],"...", *table[len(table) - 3:len(table)], "\n")
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
            if Status == "computer":
                raise Exception
            if move == 0:
                Status = "computer"
                player_pieces.append(stock_pieces[0])
                stock_pieces.remove(stock_pieces[0])
            elif move > 0 and player_pieces[move - 1][0] == table[-1][1]:
                table.append(player_pieces[move - 1])
                player_pieces.remove(player_pieces[move - 1])
                Status = "computer"
            elif move > 0 and player_pieces[move - 1][1] == table[-1][1]:
                player_pieces[move - 1].reverse()
                table.append(player_pieces[move - 1])
                player_pieces.remove(player_pieces[move - 1])
                Status = "computer"
            elif move < 0 and player_pieces[-move - 1][1] == table[0][0]:
                table = [player_pieces[-move - 1]] + table
                player_pieces.remove(player_pieces[-move - 1])
                Status = "computer"
            elif move < 0 and player_pieces[-move - 1][0] == table[0][0]:
                player_pieces[-move - 1].reverse()
                table = [player_pieces[-move - 1]] + table
                player_pieces.remove(player_pieces[-move - 1])
                Status = "computer"
            else:
                raise TypeError
        elif len(player_pieces) == 0:
            print("Status: You WIN!✔✔✔")
            print("        🎂 🎂 🎂")
            B = False
        if table[0][0] == table[-1][1]:
            count = 0
            for i in table:
                for g in i:
                    if g == table[0][0]:
                        count += 1
            if count == 8:
                print("Game Over, 8 numbers")
                B = False
    except ValueError:
        if len(pc_pieces) > 0:
            for i in pc_pieces:
                if Status == "computer":
                    if i[0] == table[-1][1]:
                            table += [i]
                            pc_pieces.remove(i)
                            Status = "player"
                    elif i[1] == table[-1][1]:
                            i.reverse()
                            table += [i]
                            pc_pieces.remove(i)
                            Status = "player"
                    elif i[1] == table[0][0]:
                            table = [i] + table
                            pc_pieces.remove(i)
                            Status = "player"
                    elif i[0] == table[0][0]:
                            i.reverse()
                            table = [i] + table
                            pc_pieces.remove(i)
                            Status = "player"
            if Status == "computer":
                if len(stock_pieces) != 0:
                    pc_pieces.append(stock_pieces[0])
                    stock_pieces.remove(stock_pieces[0])
                    Status = "player"
        else:
            print("Status: Computer WIN!✔✔✔")
            B = False
    except TypeError:
        error = ("Invalid input or wrong pieces")
    except Exception:
        error = ("Computer must move, Press Enter")
    except IndexError:
        error = ("Invalid input, number > pieces")
