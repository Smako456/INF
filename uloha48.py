import random
n=int(input("zadaj pocet cisel: "))
s=0
for i in range(n):
    a=random.randint(1, 100)
    print("cislo:", a, end=" ")
    s=s+a
priemer=s/n
print()
print("priemer:", priemer)

