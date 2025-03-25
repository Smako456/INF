p=int(str("zadaj pohlavie bez diakritiky: "))
v=int(input("zadaj vek: "))
if v<19 and p=="muz":
    print("ziak")
elif v<19 and p=="zena":
    print("ziacka")
elif v>=19 and p=="muz":
    print("student")
elif v>=19 and p=="zena":
    print("studentka")
else:
    print("nezadal si spravne udaje")


