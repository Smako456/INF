n=int(input("zadaj prirodzene cislo: "))
p=0 #inicializacia pocitadla
for i in range(1, n+1):
    if i%2!=0:
        print(i, end=", ")
        p=p+1
print()
print("pocet neparnych cisel:", p)