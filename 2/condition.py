import random

raw_input_data = input("adj meg egy számot:")
try:
    number = int(raw_input_data)
    if number < 10:
        print("ez a sz kissebb mint 10")
    else:
        print("Ez a szám nagyobb vagy engyelnő 10el")

    if number > 100:
        print("Ez a szám nagyobb mint 100")
    else:
        print("Ez a szám nem nagyobb mint 100")

    if number % 2 > 0:
        print("páratlan")
    else:
        print("páros")

    number2 = 200
    if number % number2 == 0:
        print("A", number2, "osztója a", number)
    else:

        if number2 % number ==0:
            print("A", number, "osztója a", number2)
        else:
            print("Egyik sem osztója a másiknak")

    str = "alma"
    if str[0] == str[-1]:
        print("az első és az utcsó megegyezik")
    else:
        print("nem egyezik meg")


    if number > 0:
        print("pozitív")
    else:
        if number < 0:
            print("negga")
        else:
            print("nulla")

    if number > 0:
        print("pozitív")
    elif number < 0:
        print("negga")
    else:
        print("nulla")

    str = "alma"
    if str[0].isupper():
        print("nagybetűvel kezdődik")
    else:
        print("nem nagybetűvel kezdődik")

    str2 = "almafa"
    str = "almaszár"
    if str[0:5] == str2[0:5]:
        print("Az első 5 karakter azonos")
    else:
        print("nem azonos első 5 karakter ")



    if number >= 3 and number < 17:
        print("Beleesik a szam a [3, 17) intervallumba")
    else:
        print("nem esik a szam a [3, 17) intervallumba")

    a, b, c = 2, 3, 4
    if a + b > c and a + c> b and b +c >a:
        print("lehet ezekkel az oldalakkal 3szöget szerkezteni")
    else:
        print("nem lehet ezekkel az oldalakkal 3szöget szerkezteni")



    #egy megoldás
    e, r, t = random.randint(1,100), random.randint(1,100), random.randint(1,100)

    print(e, r, t)
    if e > r and e > t:
        print(e, "A legnagyobb szám")
    if r > e and r > t:
        print(r, "A legnagyobb szám")
    if t > r and t > e:
        print(t, "A legnagyobb szám")

    if e < r and e < t:
        print(e, "A legkissebb szám")
    if r < e and r < t:
        print(r, "A legkissebb szám")
    if t < r and t < e:
        print(t, "A legkissebb szám")

    karakter = "j"

    if karakter == "a" or "á" or "e" or "é" or "i" or "í" or "o" or "ó" or "ö" or "ő" or "u" or "ú" or "ü" or "ű":
        print("magánhangzó")
    else:
        print("nem magánhanzó")


    maganhangzok = "aáeéiíoóöőüűuúAÁEÉOÓUÚÖŐÜŰ"
    if maganhangzok.find(karakter) >= 0:
        print("magánhangzó")
    else:
        print("nem magánhangzó")

    szam = random.randint(1, 5)
    if szam == 5:
        print("kiváló")
    elif szam == 4:
        print("jó")
    elif szam == 3:
        print("megfelel")
    elif szam == 2:
        print("elégséges")
    elif szam == 1:
        print("elégtelen")
    else:
        print("nem megfelelő érték")
except ValueError:
    print("Számot adjá!")








