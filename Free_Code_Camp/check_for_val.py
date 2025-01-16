def get_user_info():
    age = int(input("Enter your age: "))
    while age <= 0 or age > 120:
        print("Invalid age. Please enter a valid age.")
        age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    print("Your age is " + str(age) + " and your height is " + str(height) + " meters.")

get_user_info()