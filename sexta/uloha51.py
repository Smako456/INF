A=int(input('Zadajte cislo A (vacsie):'))
B=int(input('Zadajte cislo B (mensie):'))
if A>B:
    for i in range(A,B -1,-1):
        print(i,end=' ')
else:
    print('Chyba: A musi byt vacsie ako B')
        
