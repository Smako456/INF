import random
a=input("zadaj pre sucin N a pre sucet T: ")
if a=="N":
    c1=random.randint(0,100)
    c2=random.randint(0,100)
    vysledok=c1*c2
    print("vypocitajte:",c1,".",c2,"=")
    v=int(input())
    if v==vysledok:
        print("spravne")
    else:
        print("nespravne")

if a=="T":
    c1=random.randint(0,100)
    c2=random.randint(0,100)
    vysledok=c1+c2
    print("vypocitajte:",c1,"+",c2,"=")
    v=int(input())
    if v==vysledok:
        print("spravne")
    else:
        print("nespravne")