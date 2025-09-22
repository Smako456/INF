cislo=input("zadaj prirodzene cislo: ")
cifra=input("zadaj hladanu cifru: ")
je=False
a=0
for i in cislo:
    if cifra==i:
        je=True
        a+=1 #a=a+1
if je == True:
    print("Cifra",cifra,"sa nachadza v cisle",cislo,"a nachadza sa",a,"krat")
else:
    print("Cifra",cifra,"sa nenachadza v cisle",cislo)