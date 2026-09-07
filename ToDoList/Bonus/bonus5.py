waiting_list = ["sen", "ben", "john"]
# moze i ovdje waiting_list.sort() #sortira listu
#sort ne vraća ništa, dok replace vrača novu vrijednost, pa je potrebno dodijeliti varijabli
for i, name in enumerate(sorted(waiting_list), start=1):#enumerate ti omogućuje da vrat "i" i  "name" iz liste
    print(f"{i}.{name}")

