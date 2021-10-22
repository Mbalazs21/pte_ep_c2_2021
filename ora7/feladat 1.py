import easygui
import math
diameter_str = easygui.enterbox("A kör átmérője cmben:", title="Adatlekérés")
try:
    diameter = float(diameter_str)
    if diameter > 0:
        radius = diameter /2
        kerulet = 2*radius*math.pi
        terulet = radius ** 2 * math.pi
        easygui.msgbox(f"A {diameter} cm átmérojű kör kerülete {kerulet:.3f} cm,"
                       f"területe pedig {terulet:.3f} cm^2")
    else:
        easygui.msgbox("nem megfelelö atmerő",title="hiba" )
except ValueError:
    easygui.msgbox("nem megfelelö atmero", title="hiba")

