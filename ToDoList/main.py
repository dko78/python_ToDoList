#prompt = "Type add or show: "
#todos = []



#from unittest import case

def get_todos():
    with open("Files/todos.txt", "r") as file:
        todos = file.readlines()
    return todos


while True:
 user_action = input("Type add or show, edit, complete or exit: ")
 user_action = user_action.strip()

 if user_action.startswith("add"):  # | "display": OR operator je |
    todo = user_action[4:]+ '\n'#list slicing od 4 mjesta na dalje, da ne bi unosio add u listu
    # file = open("Files/todos.txt", "r") 
    # todos = file.readlines()#to stvori listu iz filea
    # file.close()
    todos = get_todos()

    todos.append(todo)
    
    with open("Files/todos.txt", "w") as file:
        file.writelines(todos)

 elif user_action.startswith("show"):  # | "display": OR operator je |
    todos = get_todos()

    #new_todos = [item.strip('\n') for item in todos] #list comprehension
     
    for i, item in enumerate(todos):
        row = f"{i+1}-{item.strip()}"# bolje ovako nego komplikacija gore
        print(row) 
  
 elif user_action.startswith("edit"):  
    try:    
        number = int(user_action[5:])#pretvara string u int
        todos = get_todos()
        new_todo = input("Enter new todo: ")
        todos[number-1] = new_todo + "\n"
        with open("Files/todos.txt", "w") as file:
            file.writelines(todos)
    except ValueError:
        print("Your command is not valid.")
        continue       
 elif user_action.startswith("complete"):
    try:
        number = int(user_action[9:])#uzima broj iz stringa
        
        todos = get_todos()

        todo = todos.pop(number - 1)#treba mi naziv da prije nego ga obrišem ispišem poruku

        with open("Files/todos.txt", "w") as file:
            file.writelines(todos)
        
        message = f"Todo {todo.strip()} was removed from the list."
        
        print(message)
    except IndexError:
        print("There is no item with that number.")
        continue    

 elif user_action.startswith("exit"):
   break #izlaz iz while petlje
 else:
    print("Command is not valid!")

print("Bye!")
    
#  if _:
#    print("Invalid command")
 #todos.append(todo)
 #print(todos)
#   5 puta ispiše 
#  for i in range(5):  
#     print("Pozdrav")

#liste
# items = ["a", "b", "c"]

# print(items[1])          # b
# print(items.index("c"))  # 2

# for i, x in enumerate(items):
#     print(i, x)

#files
#files.open(r"Files/todos.txt", "r")  # r = read, w = write, a = append. Kad staviš r ispred onda ignorira posebne znakove \n....
