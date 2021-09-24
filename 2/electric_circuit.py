villaynyora = 25
halozatifeszultseg = 230
villanyora_teljesitmeny = villaynyora * halozatifeszultseg

izzo = 30 # W
izzok = 5 * izzo

klima = 1500
mosogep = 1200
vasalo = 2000

osszes = klima + mosogep +izzok
print("összes eddig", osszes, "W")
print("villanyóra teljesítménye:", villanyora_teljesitmeny)

ha = osszes + vasalo
print("Lekapcsol a megszakíto?", ha > villanyora_teljesitmeny)