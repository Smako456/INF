cenatovarusDPH=float(input("Zadaj cenu s DPH: "))
DPH=float(input("Zadaj vysku DPH v percentach: "))
cenabezDPH=cenatovarusDPH/(DPH/100+100)*100 #treba doriesit
print ("cena bez DPH je: ", cenabezDPH)