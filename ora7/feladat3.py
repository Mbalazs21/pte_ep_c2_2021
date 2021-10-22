import easygui
import random


easygui.msgbox("Találja ki a számot (1-99)!\n 6 lehetősége van.",
               ok_button="induljon a játék!")
tries = 0
try:
    bot_number = random.randint(1,99)
    print(bot_number)
    number = easygui.enterbox("1-99")
    while number < 6 and number != bot_number:
        if number == 0:
            easygui.msgbox("üresen hagyta a mezőt!", title="hiba")
            tries = tries +1
        if number < bot_number:
            easygui.msgbox("nagyobb számra gondoltam")
        if number > bot_number:
            easygui.msgbox("kisebb számra gondoltam")
        if number == bot_number:
            easygui.msgbox("Sikeresen eltalálta!", title="yey")
except ValueError:
    easygui.msgbox("nem megfelelő értéket adott meg!", title="hiba")

