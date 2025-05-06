c=int(input("zadaj prirodzene cislo: "))
if c==1:
    print("cislo 1 nie je ani prvocislo ani zlozene")
else:
    pd=0
    for i in range(1, c+1):
        if c%i==0:
            pd+=1
    if pd==2:
        print(c,"je prvocislo")
    else:
        print(c,"je zlozene")

