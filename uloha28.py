b=int(input("Zadaj body: "))
if b>=90:
    print("A")
elif 80<=b<90:
    print("B")
elif 70<=b<80:
    print("C")
elif 60<=b<70:
    print("D")
elif 50<=b<60:
    print("E")
elif 0<=b<50:
    print("FX")
else:
    print("Zle zadane body")