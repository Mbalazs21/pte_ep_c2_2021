number = 5
number2 = number * 2
print("A number változó értéke: ", number, "\b Ha megszorzom kettovel: ", number2,"\b-t kapok")
print("A number változó értéke: ", number, " Ha megszorzom kettovel: ", number2,"-t kapok", sep="")
print(f"A number változó értéke: {number}  Ha megszorzom kettovel: , {number2},-t kapok")
print("A number változó értéke: {} Ha megszorzom kettovel: {}-t kapok".format(number,number2))

#igazítások


print(f"A number változó értéke: {number:<3}  Ha megszorzom kettovel: , {number2:>5},-t kapok")
print("A number változó értéke: {:^3} Ha megszorzom kettovel: {:^5}-t kapok".format(number,number2))

#számformátumok
number = 125
print(f"A szám bináris alakja:{number:b} az oktális alakja: {number:o} a decimális alakja: {number:d} hexadecimális {number:x} és {number:x}".format(number, number,number,number, number))
