with open("Files/todos.txt", "a") as file:
    file.write("meet Tom\n")

with open("Files/todos.txt", "r") as file:
    todos = file.readlines()

print(len(todos))

# In the coding area, we have defined a list of languages. Add some code that:

# (1) iterates over the list using a for-loop,

# (2) creates a new text file in each iteration using a with-context manager,

# (3) each file should be named according to the current item (i.e., English.txt, German.txt, and Spanish.txt).

# (4) the content of each file should be the item of the list (e.g., the content of the file English.txt should be English).

languages = ['English', 'German', 'Spanish']

d = len(languages)
for i in range(d):  
    with open(f"Files/{languages[i]}.txt", "w") as file:
        file.write(languages[i])


# In the coding area there is a story.txt file tab that contains some text. Your task is to make a copy of the story.txt file. Here are the exact steps:

# (1) Read the story.txt file using a with-context manager and store its text in a string variable.

# (2) Create a new story_copy.txt file using a second with-context and write the string variable in the file.        
with open("story.txt", "r", encoding="utf-8") as file:
    text = file.read()

with open("story_copy.txt", "w", encoding="utf-8") as file:
    file.write(text)