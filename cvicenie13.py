n=input("zadaj cislo: ")
p=0
ne=0
for i in n:
    if int(i)%2==0:
        p+=1
    if int(i)%2!=0:
        ne+=1
print("pocet parnych cifier je: ", p,";pocet neparnych cifier je: ", ne)