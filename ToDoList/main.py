#prompt = "Type add or show: "
todos = []
while True:
 user_action = input("Type add or show, edit or exit: ")
 user_action = user_action.strip()
 match user_action:
  case "add":
    todo = input("Enter a todo: ")
    todos.append(todo)
  case "show":  # | "display": OR operator
   for item in todos:
    item = item.title()
    print(item) 
  case "edit":  
    number = int(input("Number of the todo to edit: "))
    new_todo = input("Enter a new todo: ")  
    todos[number-1] = new_todo  
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

