password = input("Unesi lozinku: ")

checks = {
    "veliko slovo": False,
    "malo slovo": False,
    "broj": False,
    "poseban znak": False
}

for char in password:
    if char.isupper():
        checks["veliko slovo"] = True
    elif char.islower():
        checks["malo slovo"] = True
    elif char.isdigit():
        checks["broj"] = True
    elif char in "!@#$%^&*()_+-=[]{}|;':\",./<>?":
        checks["poseban znak"] = True

if len(password) < 8:
    print("Lozinka mora imati barem 8 znakova.")
elif all(checks.values()):
    print("Lozinka je valjana.")  
else:
    print("Lozinka nije valjana. Nedostaje:")
    for uvjet, ispunjen in checks.items():
        if not ispunjen:
            print(f"- {uvjet}")