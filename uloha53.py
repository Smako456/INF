x=int(input('Zadajte zaklad:'))
y=int(input('Zadajte exponent:'))
vysledok=1
for i in range(y):
    vysledok=x*vysledok

print('Vysledok:',x,"^",y,"je",vysledok)    
