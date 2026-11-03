def get_average():
    with open('todo_list/ToDoList/Bonus/Files/data.txt', 'r') as file:
        data = file.readlines()

    values = data[1:]  # Skip the header line
    values = [float(value.strip()) for value in values]  # Convert to float and remove whitespace
    average_local = sum(values) / len(values) if values else 0  # Calculate average, handle empty list
    return average_local


average = get_average()
print(f"The average is: {average}")


