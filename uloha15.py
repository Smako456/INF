import random
r=int(input("zadaj riadky: "))
s=int(input("zadaj stlpce: "))
for i in range(1,r+1):
    for j in range(s):
        print(random.randint(0,1), end="")
    print()