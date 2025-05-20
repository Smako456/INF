n=int(input("zadaj cislo: "))
d=0
for i in range(1,n+1):
    if n%i==0:
        print("delitel je:", i)
        d+=1
print("cislo ma", d, "delitelov")