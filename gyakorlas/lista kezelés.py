
names_list = []
i = 0
roundK = 1
print("Adjon meg öt nevet!")
while i <= 4:
    names = input("Kérem adja meg az "+str(roundK)+". nevet:")
    names_list.append(names)
    i += 1
    roundK += 1
print("az adott nevek:", names_list)
names_list.sort()
print("az adott nevek ABC sorrendben: ", names_list)
print("A harmadik név: ", names_list[2])
new_row = input("Kérem adjon meg egy sorszámot amelyiket ki akarja cserélni: ")

new_name = input("Kérem adjon meg egy új nevet, amelyikre ki akarja cserélni: ")
del(names_list[int(new_row)])
names_list.insert(int(new_row), new_name)
print("Az új lista elemei:", names_list)
