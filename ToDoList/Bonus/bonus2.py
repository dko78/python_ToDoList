password = input("Enter your password: ")
brojac = 0
while password != "proba123" and brojac < 3:
    print("Incorrect password. Please try again.")
    password = input("Enter your password: ")
    brojac = brojac + 1
    print(f"You have {3 - brojac} attempts left.")

print("Access granted. Welcome!")