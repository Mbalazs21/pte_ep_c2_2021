
a = int(input("Add meg a mértani sorozat első tagját:"))
q = int(input("Add meg a mértani sorozat hányadosát:"))

n = int(input("Add meg a mértani sorozat kívánt tagját:"))
nn = n - 1
answer = a * (q ** int(nn))


print("A kívánt hatványérték:", answer)