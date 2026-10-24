countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for country in countries:
    # print(country)
     file = open(country.txt, "w")
     file.write(country)
     file.close()

for i in range(len(countries)):
     print(countries[i])