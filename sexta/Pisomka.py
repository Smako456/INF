k=int(input("Zadaj teplotu v Kelvinoch (cele cislo):"))
c=k-273

if c>0:
    print("teplota v Kelvinoch:",k)
    print("teplota v stupnoch Celsia:",c)
    print("teplota je kladna")

if c<0:
    print("teplota v Kelvinoch:",k)
    print("teplota v stupnoch Celsia:",c)
    print("teplota je zaporna")

if c==0:
    print("teplota v Kelvinoch:",k)
    print("teplota v stupnoch Celsia:",c)
    print("teplota je nulova")
