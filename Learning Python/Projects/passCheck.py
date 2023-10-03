name = input("Enter your UserName: ")
password = input("Enter your password: ")
length = len(password)
star = length * "*"
print(f"Hello {name}, your password {star} is {length} letters long")