class User:

    def __init__(self, first_name, last_name, age):

        """Constructor with all the required attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        self.login_attempts = 0

    def describe_user(self):

        """Give a detail of information about the user"""

        full_name = f"{self.first_name} {self.last_name}"
        return f"Full name: {full_name}, Age: {self.age}"
        
    def greet_user(self):

        """Greets user with their details"""
        full_name = f"{self.first_name} {self.last_name}"
        return f"Hello {full_name}! You are {self.age} years old"
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Alex", "Jones", "35")

print(user1.greet_user())

