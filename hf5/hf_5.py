file = "file_hf5.txt"
fileobject = open(file, "r")
read_all_row = fileobject.readlines()
read_all_characters = fileobject.readlines()


row1 = fileobject.readline()
counter = len(row1)







all_row = len(read_all_row)
print("Összes sor:", all_row)
print("Összes karakter:", counter)


fileobject.close()




