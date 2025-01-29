
while True:
    username = input("Type your username: ").replace(" ", "")

    if not username.isalpha():
        print("Username cannot contain numbers.")
    elif len(username) > 12:
        print("Username must be 12 characters or less.")
    #A função find retorna -1 caso tenha espaços
    elif not username.find(" ") == -1:
        print("Username cannot have spaces")
    else:
        break
print(f"Your username is: {username}")