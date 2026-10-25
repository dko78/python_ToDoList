user_action = input("Type add or show, edit, complete or exit: ")

user_action = user_action.strip()

if "add" in user_action:
    print("Add command:" + user_action[4:])  # list slicing od 4 mjesta na dalje, da ne bi unosio add u listu
