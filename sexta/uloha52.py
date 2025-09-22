n= int(input('Zadajte prirodzene cislo n:'))
if n>=1:
    for i in range(1,n+1):
        print(2**i,end=' ')
else:
    print('chyba: n musi byt prirodzene cislo (vacsie alebo rovne 1)')
    
