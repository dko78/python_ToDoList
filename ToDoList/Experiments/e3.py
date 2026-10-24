filenames = ["file1.txt", "file2.txt", "file3.txt"]

filenames = [filename.replace('.txt', '.csv') for filename in filenames]
print(filenames)

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

usernames = ["john 1990", "alberta1970", "magnola2000"] 

usernames = [len(username) for username in usernames]
print(usernames)

user_entries = ['10', '19.1', '20']

user_entries = [float(entry) for entry in user_entries]
print(user_entries)

# We have defined a numbers variable in the coding area. Add some code that:

# (1) multiplies each number of the list by 2, and

# (2) prints out the updated list.

# Here is the expected output:
numbers = [10, 20, 30]
numbers = [number * 2 for number in numbers]
print(numbers)

# Extend the given code so it prints out the sum of the numbers. Note that the numbers are currently string types.
user_entries = ['10', '19.1', '20']

user_entries = [float(entry) for entry in user_entries]
print(sum(user_entries))
#ili
total = sum(float(entry) for entry in user_entries)
print(total)
