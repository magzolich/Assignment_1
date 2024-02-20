#task 2 Implement a system check for new users registering on a UBS-webmail that recently introduced.

while True:
    # Prompt user for input
    name = input("Please provide your name: ")
    email = input("Please provide your email: ")

    # Validate user name
    if any(char.isdigit() for char in name):
        print("Name cannot include numeric characters. Please try again.")
        continue
    elif len(name) > 15:
        print("Name cannot exceed 15 characters. Please try again.")
        continue

    # Validate email address
    if not email.startswith(name.lower()):
        print("Email address must start with the name in lower case. Please try again.")
        continue
    elif not email.endswith('@ubs.com'):
        print("Email address must end with '@ubs.com'. Please try again.")
        continue
    elif '_' not in email:
        print("Email address must include an underscore ('_'). Please try again.")
        continue
    elif ' ' in email:
        print("Email address cannot contain whitespaces. Please try again.")
        continue

    # If all validations passed, break out of the loop
    break

# Print success message
print("User name and email address are valid. Registration successful!")
