todos = []
while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo + "\n")
        case "show":  # | "display": OR operator je |
            for i, item in enumerate(todos):
                row = f"{i+1}-{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break  # izlaz iz while petlje
           
        case _:
            print("Invalid command")

             