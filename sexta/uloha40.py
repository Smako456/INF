import random
n=int(input("zadaj opakovania: "))
p=0
for i in range(n):
    a=random.randint(1, 100)
    if a%2==0:
        print(a, end=", ")
        p=p+1
print()
print("pocet parnych cisel:", p)