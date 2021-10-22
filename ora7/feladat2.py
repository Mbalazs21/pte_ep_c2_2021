import easygui

years_str = easygui.enterbox("Adjon meg egy évszámot:", title="Adatlekérés")

eredmeny = "eredmény"
try:
    year = int(years_str)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                easygui.msgbox("A megadott év szövőév", title=eredmeny)
            else:
                easygui.msgbox("Az érték nem osztható 400 al", title="nem szoko év")
        else:
            easygui.msgbox("Az érték nem osztható 100 al", title=eredmeny)
    else:
        easygui.msgbox("Az érték 4el oszthato", title=eredmeny)
except ValueError:
    easygui.msgbox("nem megfelelö érték", title="hiba")
