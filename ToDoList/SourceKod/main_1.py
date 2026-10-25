# Optimization: use elif so only ONE branch runs per iteration. With
# plain `if`s, Python checks every condition even after one matched —
# wasted work.
#
# Also: extend the same single-line pattern to edit and complete:
#   "edit 2"      -> user_action[5:] -> "2"
#   "complete 2"  -> user_action[9:] -> "2"
# Wrap with int() to turn the slice into a number.
#
# Add an `else` branch for unrecognized commands so the user gets a
# clear "Command is not valid." message instead of silent failure.

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[9:])
        index = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid.")
print("Bye!")
