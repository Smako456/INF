x=int(input("Zadaj suradnicu x: "))
y=int(input("Zadaj suradnicu y: "))
if x>0 and y>0:
    print("1. kvadrant")
elif x<0 and y>0:
    print("4. kvadrant")
elif x<0 and y<0:
    print("3. kvadrant")
elif x>0 and y<0:
    print("2. kvadrant")

if x==0 and y==0:
    print("V strede")
elif x==0 or y==0:
    print("Na osi")
