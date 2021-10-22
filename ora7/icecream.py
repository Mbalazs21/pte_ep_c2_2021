
from easygui import *

user_response=msgbox("Hello There!", title="hello", ok_button="Hi bitch!",image="python_logo.png")
print(user_response)

flavor = buttonbox("What is your favourite ice cream flavor?", title="icecream",
                   choices=['Vanilla[1]', 'Chocolate[2]', 'Strawberry[3]', 'Cherry[4]'],
                   default_choice="Vanilla[1]")
msgbox("You picked " + flavor)

flavor = choicebox("what is your favourite ice cream flavor?", title="icecream2",
                   choices=['Vanilla', 'Chocolate', 'Strawberry', 'Cherry'], preselect=1)
msgbox("You picked " + flavor)

flavor = enterbox("what is your favourite ice cream flavor?", title="icecream3",default="körte",image="python_logo.png")
msgbox("You picked " + flavor)
if flavor is not None:
    msgbox("you picked" + flavor)
else:
    print("cancel gombra nyomott a felhasználó")