filenames = ["1.data1.txt", "2.data2.txt"]

print(len(filenames))
print(type(filenames))

for filename in filenames:
    filename = filename.replace(".","_", 1)
    print(filename)

# ver 2 
print("*****************************************************************")

for i in range(len(filenames)):
    filenames[i] = filenames[i].replace(".", "_", 1)
    print(filenames[i])     

filenames_tuple = ("1.data1.txt", "2.data2.txt")#tuples are immutable, liste su mutable

s = "A B   C"
s2 = s.replace(" ", "")
print(s2)  # ABC
print("split:", s.split())        # ['A', 'B', 'C']

s2 = "".join(s.split())
print(s2)  # ABC



s = " A \tB\n C "

print(s.split())        # ['A', 'B', 'C']

print("".join(s.split()))  # 'ABC'

# separator.join(iterable) iterable mora sadržavati stringove.
# "-".join(["a", "b", "c"])   # "a-b-c"
# "".join(["a", "b", "c"])    # "abc"
# " ".join(["John", "Smith"]) # "John Smith"

# a = [1, 2, 2, 3]
# len(a)        # 4
# a.count(2)    # 2

#slicing
#first_two = list_1[:2] # ne uklljučuje 2 ( samo 0 i 1)

print("#raspakiravnje u varijable tuple")
person = ("John", 25, "USA")
name, age, country = person

print(name)     # John
print(age)      # 25
print(country)  # USA

print("#raspakiravnje u varijable lista")
items = ["John", 25, "USA"]
name, age, country = items
