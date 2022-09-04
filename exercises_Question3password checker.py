password =input("enter your password")
if len(password) < 8 or password.lower() == password or password.upper() == password or password.isalnum()\
  or not any(i.isdigit() for i in password):
    print("your password is weak")
else:
	print("your password is strong")

