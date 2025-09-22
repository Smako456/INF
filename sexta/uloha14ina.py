n=int(input("zadaj prirodzene cislo: "))
a=1
for i in range(1,2*n):
    if i<=(n):
        print((i-1)*" ",n*"*")
    elif i>(n):
        a+=1
        print((n-a)*" ",n*"*")