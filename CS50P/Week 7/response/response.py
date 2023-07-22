import validators

user_email = input("What is your email address? ").strip()

if validators.email(user_email):
    print("Valid")
else:
    print("Invalid")