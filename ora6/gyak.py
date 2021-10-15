kmh = int(input("kérem adjon meg egy sebességet km/h-ban"))
difference = 0.277778
ms = kmh * difference
ms = round(ms, 2)
print("Az adott km/h m/s-ban:", ms)

#vaagy igy:
try:
    kmh = float(input("kérem adjon meg egy sebességet km/h-ban"))
    ms = kmh * 1000/3600
    print(f"A{kmh} sebesseg az {ms} felel meg")
except:
    print("sorry")



