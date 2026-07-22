#prompt = "Type add or show: "
todos = []
while True:
 user_action = input("Type add or show, or exit: ")
 user_action = user_action.strip()
 match user_action:
  case "add":
    todo = input("Enter a todo: ")
    todos.append(todo)
  case "show":  # | "display": OR operator
   for item in todos:
    item = item.title()
    print(item) 
  case "exit":
   break
  case _:
   print("Invalid command")
 #todos.append(todo)
 #print(todos)

