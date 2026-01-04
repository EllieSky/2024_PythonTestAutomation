attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_name = input("Please enter your name:   ")
    attempts += 1

    # check length
    if len(user_name) < 5:
        remaining = max_attempts-attempts
        print(f"x User name should be at least 5 characters")
        print(f"Attempts remaining: {remaining}\n")
        continue

    if user_name.isdigit():
        remaining = max_attempts - attempts
        print("✗ User name cannot be all numbers")
        print(f"Attempts remaining: {remaining}\n")
        continue  # Go back to start of loop

    # all checks passed
    print("User name is valid!")
    break

if attempts > max_attempts:
    print("Account locked - too many failed attempts")
    print("Please contact support.\n")
    exit()

attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password = input("Enter your password:    ")
    attempts += 1

    if len(password) < 8:
        remaining = max_attempts - attempts
        print("x Password should be at least 8 characters")
        print(f"Attempts remaining: {remaining}\n")
        continue


    # check if contains at least 1 number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if not has_number:
        remaining = max_attempts - attempts
        print("x Password must contain at least one number")
        print("Please try again.\n")
        print(f"Attempts remaining: {remaining}\n")
        continue

    # All checks passed!
    print("✓ Password is valid\n")
    break
if attempts >= max_attempts:
    print("❌ ACCOUNT LOCKED - Too many failed password attempts")
    print("Please contact support.\n")
    exit()

print("\n✓✓✓ LOGIN CREDENTIALS ACCEPTED ✓✓✓")


print("="*50)
print("LOGIN SUMMARY")
print("="*50)
print(f"Username: {user_name}")
print(f"Password length: {len(password)} characters")
print(f"Password: {'*' * len(password)}")  # Hide actual password
print("="*50)
print("\n✓✓✓ LOGIN CREDENTIALS ACCEPTED ✓✓✓")