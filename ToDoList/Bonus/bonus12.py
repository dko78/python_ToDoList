feet_inches = input("Enter height in feet and inches : ")


def convert_to_inches(feet_inches):
   #parts = feet_inches.split(" ")
    feet, inches = feet_inches.split(" ")#možeš i ovako odjednom
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters

total_meters = convert_to_inches(feet_inches)
print(f"Total height in meters: {total_meters}")    

#neki drugi primjer
def strength(password):
      if (
        len(password) >= 8
        and any(ch.isupper() for ch in password)
        and any(ch.isdigit() for ch in password)
    ):
        return "Strong Password"

# (1) takes a list as an argument

# (2) returns the average value of the list items.

# For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.

def myAverage(lista):
    return sum(lista) / len(lista)  


def foo(items):
    total = 0
    count = 0

    for x in items:
        total += x
        count += 1

    return total / count

brojevi = [10, 20, 30, 40]

for i, broj in enumerate(brojevi):
    print(i, broj)
