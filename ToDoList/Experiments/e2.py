user_prompt ="Upiši to-do:"

x = 0

todos = []
while x < 5:
    todo = input(user_prompt)
    print(todo.capitalize())#to je methoda zato (), title() svako slovo u recenici
    todos.append(todo)
    x = x + 1

print(todos)
    