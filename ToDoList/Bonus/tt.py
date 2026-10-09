countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for country in countries:
    file = open(country.txt, "w")
    file.write(country)
    file.close()