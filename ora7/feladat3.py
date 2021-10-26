import easygui
import random
easygui.msgbox("Találja ki a számot (1-99)!\n 6 lehetősége van.",
               ok_button="induljon a játék!")
tries = 6
try:
    bot_number = random.randint(1, 99)
    #print(bot_number)
    number = int(easygui.enterbox(str(tries) + "lehetősége van", title="játék"))
    tries = tries - 1
    while number != bot_number and tries >= 1:
        if number > bot_number:
            number = int(easygui.enterbox("kisebb számra gondoltam\n" + str(tries) + "lehetősége van", title="játék"))
            tries = tries - 1
        if number < bot_number:
            number = int(easygui.enterbox("nagyobb számra gondoltam\n" + str(tries) + "lehetősége van", title="játék"))
            tries = tries - 1
    if tries == 0:
        easygui.msgbox("Elfogytak a lehetőségei!  \n:c\nA keresett szám:" + str(bot_number), title="vesztett")
    if number == bot_number:
        easygui.msgbox("Gratula! :)", title="Nyert!")
except ValueError:
    easygui.msgbox("nem megfelelő értéket adott meg!", title="hiba")