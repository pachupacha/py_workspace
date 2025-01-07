username_list = ["Peter123", "Sam.321", "Connor-309", "Mary@Bunny"]
password_list = ["HappyGilmoure33", "Spider-Man78", "11223344xX", "Ññ@q5058"]

max_attemps = 3
attemps = 0
validation = False

while attemps < max_attemps:
    username = input("User: ")
    password = input("Password: ")

    for i in range(len(username_list)):
        if username_list[i] == username and password_list[i] == password:
            validation = True
            print(f"Welcome, {username}.")
            if validation == True:
                exit()
    else:
        attemps += 1
        remaining_attemps = max_attemps - attemps
        if remaining_attemps > 0:
            print(f"Access Denied. {remaining_attemps} tryouts left.")
        else:
            print("Access Denied.")
            exit()
