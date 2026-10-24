#prompt = "Type add or show: "
#todos = []



from unittest import case


while True:
 user_action = input("Type add or show, edit, complete or exit: ")
 user_action = user_action.strip()

 if "add" in user_action:
    todo = input(user_action[4:] + "\n")#list slicing od 4 mjesta na dalje, da ne bi unosio add u listu

    # file = open("Files/todos.txt", "r") 
    # todos = file.readlines()#to stvori listu iz filea
    # file.close()
    with open("Files/todos.txt", "r") as file:
        todos = file.readlines()#to stvori listu iz filea

    todos.append(todo)
    
    with open("Files/todos.txt", "w") as file:
        file.writelines(todos)

 if "show" in user_action:  # | "display": OR operator je |
    with open("Files/todos.txt", "r") as file:
        todos = file.readlines()

    #new_todos = [item.strip('\n') for item in todos] #list comprehension
     
    for i, item in enumerate(todos):
        row = f"{i+1}-{item.strip()}"
        print(row) 
  
 if "edit" in user_action:  
    number = int(input("Number of the todo to edit: "))
    with open("Files/todos.txt", "r") as file:
            todos = file.readlines()#to stvori listu iz filea
    new_todo = input("Enter new todo: ")
    todos[number-1] = new_todo + "\n"
    with open("Files/todos.txt", "w") as file:
        file.writelines(todos)

 if "complete" in user_action:
    number = int(input("Number of the todo to complete: "))
    
    with open("Files/todos.txt", "r") as file:
            todos = file.readlines()#to stvori listu iz filea

    todo = todos.pop(number - 1)#treba mi naziv da prije nego ga obrišem ispišem poruku

    with open("Files/todos.txt", "w") as file:
        file.writelines(todos)
    
    message = f"Todo {todo.strip()} was removed from the list."
    
    print(message)

 if "exit" in user_action:
   break #izlaz iz while petlje
    
 if _:
   print("Invalid command")
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
