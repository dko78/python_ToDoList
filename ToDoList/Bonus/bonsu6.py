from pathlib import Path
import os
from pathlib import Path


file = open(r"C:\GITcloud\EBC_OBRADE_DEPOZITA\Database_Update\VIBIS\AML_neprihvatljiv.sql", "r")#imaš r, w, i a! Append daje na kraj , ne prepisuje postojeće, kad iza imaš file.write("abc")
print(type(file))
sadrzaj = file.read()
file.close()
#test
#print("test", sadrzaj)

#


#

putanja = Path(__file__).resolve().parent.parent / "Files" / "doc.txt"
print('putanja je:', putanja)
with open(putanja, "r", encoding="utf-8") as file:
    sadrzaj = file.read()

print(sadrzaj)

#  sadrzaj = file.read() vs with open(putanja, "r", encoding="utf-8") as file:
                               # sadrzaj = file.read()
# Može i bez with, ali onda moraš ručno zatvoriti fajl.
# with je preporučen jer automatski zatvori fajl, čak i ako se desi greška.
# Bez with:
# file = open(putanja, "r", encoding="utf-8")
# sadrzaj = file.read()
# file.close()
# Sa with (bolje):
# with open(putanja, "r", encoding="utf-8") as file:
#     sadrzaj = file.read()
# Dakle, sadrzaj = file.read() može, ali file mora prethodno biti otvoren, i treba ga zatvoriti.

#zadatak
file = open(putanja, "r")
todos = file.readlines()
file.close
for item in todos:
    print(item.strip("\n"))


#
file = open('logs.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.write('171.131.104.108 POST 2.143')
file.close()

