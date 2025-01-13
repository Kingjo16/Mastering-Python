print("Welcome to My Town City!")
password = input("Please input your password: ")

while True:
    confirm_password = input("Please confirm your password: ")
    if confirm_password == password:
        print("Password Confirmed!")
        break
    else:
        print("Password Denied! Please try again.")
