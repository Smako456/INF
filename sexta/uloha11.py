c1=float(input("zadaj prve cislo: "))
c2=float(input("zadaj druhe cislo: "))
c3=float(input("zadaj tretie cislo: "))

if (c1>=c2) and (c1>=c3):
    print("najvacsie je: ",c1)
if (c2>=c1) and (c2>=c3):
    print("najvacsie je: ",c2)
if (c3>=c2) and (c3>=c1):
    print("najvacsie je: ",c3)
