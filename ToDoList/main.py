#prompt = "Type add or show: "
todos = []
while True:
 user_action = input("Type add or show, or exit: ")
 match user_action:
  case "add":
    todo = input("Enter a todo: ")
    todos.append(todo)
  case "show":
   print(todos)
  case "exit":
   break
  case _:
   print("Invalid command")
 #todos.append(todo)
 #print(todos)

