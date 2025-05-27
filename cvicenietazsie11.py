n= int(input("zadaj prirodzene cislo: "))
x=(n*2)-1
m=0
for i in range(1, n+1):
    print((i-1)*" ",(x-m)*"*",(i-1)*" ")
    m+=2