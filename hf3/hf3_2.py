product = input("Adja meg a termék árát:\n")
ten = 0.1
tweny = 0.2


cost = int(product)
if cost < 10000:
    print("A termék ára:", cost,"Ft")
    print("A kedvezmény: 10%")
    print("A termék ára az adott kedvezménnyel:", cost - (cost * ten), "Ft")

else:
    print("A termék ára:", cost, "Ft")
    print("A kedvezmény: 20%")
    print("A termék ára az adott kedvezménnyel:", cost - (cost * tweny), "Ft")

