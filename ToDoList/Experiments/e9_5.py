uvjeti ={
    "povrsina:": False,
    "prilaz": False,
    "legalanost": False,
}#dictonary

povrsina = int(input("Unesi povrsinu: "))
prilaz = input("Unesi prilaz:DA/NE ")
legalnost = input("Unesi legalnost:DA/NE ")

if povrsina > 10000:
    uvjeti["povrsina:"] = True
if prilaz.upper() == "DA":
    uvjeti["prilaz"] = True
if legalnost.upper() == "DA":
    uvjeti["legalanost"] = True

if all(uvjeti.values()):
    print("Zadovoljava uvjete")
else:
    print("Ne zadovoljava uvjete. Nedostaje:")
    for uvjet, ispunjen in uvjeti.items():
        if not ispunjen:
            print(f"- {uvjet}")    