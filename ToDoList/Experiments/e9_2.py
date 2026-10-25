password = input("Enter your password: ")

result = []

if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    for char in password:
        if char.isupper():
            result.append("Uppercase letter found.")
        elif char.islower():
            result.append("Lowercase letter found.")
        elif char.isdigit():
            result.append("Digit found.")
        elif char in "!@#$%^&*()_+-=[]{}|;':\",./<>?":
            result.append("Special character found.")

    if len(result) == 4:
        print("Password is valid.")
    else:
        print(result[0] + ' ' + "Password is invalid. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")    