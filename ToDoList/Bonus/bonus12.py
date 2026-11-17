feet_inches = input("Enter height in feet and inches : ")


def convert_to_inches(feet_inches):
   #parts = feet_inches.split(" ")
    feet, inches = feet_inches.split(" ")#možeš i ovako odjednom
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters

total_meters = convert_to_inches(feet_inches)
print(f"Total height in meters: {total_meters}")    