a = str(input("Kérek egy szót:"))

last = len(a)-1
front = len(a) - last


if a[0] == a[last]:
    if a[front] == a[last-1]:
        if a[front+1] == a[last - 2]:
            if a[front+2] == a[last - 3]:
                print("Ez palindrom")
            else:
                print("Ez nem palindrom")
        else:
            print("Ez nem palindrom")
    else:
        print("Ez nem palindrom")
else:
    print("Ez nem palindrom")

