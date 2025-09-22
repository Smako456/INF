n=int(input("zadaj pocet znamok: "))
x=0
for i in range(n):
    a=int(input("zadaj znamku: "))
    x=x+a
p=x/n
print("Priemer znamok je:", round(p,2))