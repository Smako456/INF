cenaBezDPH=float(input("zadaj cenu tovaru bez DPH: "))
DPH=int(input("zadaj vysko DPH v precentach: "))
cenaSDPH=cenaBezDPH*DPH/100+cenaBezDPH
print("cena tovaru s DPH je", cenaSDPH, "€")
