import random
n=int(input("zadaj pocet hodov: "))
s=0
for i in range(n):
    a=random.randint(1, 6)
    print("hod:", a, end=" ")
    if a==6:
        s=s+1
print()
print("pocet hodov 6:", s)