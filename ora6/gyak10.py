import random



is_winner = False
while not is_winner:
    try:
        player = int(input("Válassz kő(1), papír(2) vagy olló(3) közül!:"))
        bot = random.randint(1,3)
        print(player, bot)
        if player == bot:
            print("döntetlen")
        elif (player == 2 and bot == 1) or (player == 3 and bot == 2) or(player == 1 and bot == 3):
            print("grat nyertél")
            is_winner = True
        elif (player == 1 and bot == 2) or (player == 2 and bot == 3) or(player == 3 and bot == 1):
            print("nem nyertél csicska")
        else:
            print("newm megfelelo érték")
    except ValueError:
        print("newm megfelelo érték")
