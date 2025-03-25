a=int(input("Zadaj cislo mesiaca: "))
if 3<=a<=5:
    print("Jar")
elif 6<=a<=8:
    print("Leto")
elif 9<=a<=11:
    print("Jesen")
elif a in (1, 2, 12): 
    print("Zima")
else :
    print("to neni mesiac")