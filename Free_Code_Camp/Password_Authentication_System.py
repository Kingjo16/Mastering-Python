# Sequential Step: Input collection
print("Welcome to the Secure System!")
correct_password = "python123"  # Predefined correct password
attempts = 0
max_attempts = 3

# Repeated Step: Allow up to 3 attempts to enter the correct password
while attempts < max_attempts:
    password = input("Enter your password: ")
    attempts += 1  # Increment attempt count

    # Conditional Step: Check if the entered password is correct
    if password == correct_password:
        print("Access Granted. Welcome!")
        break  # Exit loop on success
    else:
        print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")

# Conditional Step: If all attempts are used, deny access
if attempts == max_attempts and password != correct_password:
    print("Access Denied. Too many incorrect attempts.")