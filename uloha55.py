import random
p=int(input("zadaj pocet cisel: "))
ma=-101
mi=101
x=0
y=0
for i in range(p):
    a=random.randint(-100,100)
    print(a, end=", ")
    if a>ma:
        ma=a
        x=i+1
    if a<mi:
        mi=a
        y=i+1
print()
print("najvacsie:", ma, "je na",x,"pozicii")
print("najmensie:", mi, "je na",y,"pozicii")
