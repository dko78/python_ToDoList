date = input("Upiši datum   : ")
mood = input("Upiši raspoloženje: ")
journal_entry = input("Upiši dnevnički zapis: \n  ")

with open(f"Journal/{date}.txt", "a", encoding="utf-8") as file:
    file.write(f"Datum: {date}\n")
    file.write(f"Raspoloženje: {mood}\n")
    file.write(f"Dnevnički zapis: {journal_entry}\n")