password = input("Enter your password: ")
brojac = 0
while password != "proba123":
    print("Incorrect password. Please try again.")
    password = input("Enter your password: ")
    brojac = brojac + 1
    #print(f"You have {5 - brojac} attempts left.")

print("Access granted. Welcome!")