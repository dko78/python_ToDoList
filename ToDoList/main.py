#prompt = "Type add or show: "
#todos = []
while True:
 user_action = input("Type add or show, edit, complete or exit: ")
 user_action = user_action.strip()
 match user_action:
  case "add":
    todo = input("Enter a todo: ") + "\n"
    file = open("Files/todos.txt", "r") 
    todos = file.readlines()#to stvori listu iz filea
    file.close()

    todos.append(todo)
    
    file = open("Files/todos.txt", "w")
    file.writelines(todos)
    file.close()
  case "show":  # | "display": OR operator je |
    file = open("Files/todos.txt", "r") 
    todos = file.readlines()
    file.close()
    for i, item in enumerate(todos):
        row = f"{i+1}-{item.strip()}"
        print(row) 
  
  case "edit":  
    number = int(input("Number of the todo to edit: "))
    new_todo = input("Enter a new todo: ")  
    todos[number-1] = new_todo 
  case "complete":
    number = int(input("Number of the todo to complete: "))
    todos.pop(number-1)
  case "exit":
   break #izlaz iz while petlje
  case _:
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
