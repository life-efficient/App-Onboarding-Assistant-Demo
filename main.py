# %%
# APP ONBOARDING ASSISTANT

# take user input
name = input("What's your name?")
age = input("What's your age?")
username = input("What's your username?")
location = input("What's your location?")
# %%

print(f"Can you confirm that your name is {name}?")
confirmation = None
while confirmation != "Y":
    name = input("What's your name?")
    confirmation = input("Enter Y/N\n")
print("All good, let's move on")

# filling in database

# %%
# OOP


class User:
    def __init__(self, name, age):  # remove need to call this manually
        self.name = name  # pass in user attributes as parameters upon initialisation
        self.age = age  # define all user attributes here
        print(self.name)

    def print_nicely(self, prefix=None):  # TODO print the user nicely
        print(f"Hey the name is {self.name}")
    # TODO save to file

    # TODO load from file (using static method - warning - more advanced)

    def my_function2(self):
        print("I am being called!")
        print(self.name)
        return True

    def my_function(param1, param2):
        print("I am being called!")
        return True


# TODO define onboarding inside function
# TODO call onboarding to get and validate user attributes
# TODO pass user attributes to user class to initialise new user
# TODO create signup method
# TODO create login method

josh = User()
josh.print_nicely()
# josh.set_up("Josh")
# print(josh.name)
# josh.my_function2()

# %%
# harry = User()
# harry.set_up("Harry")
sam = User("Sam", 10)
sam.__init__("Sam", 10)  # DO NOT DO THIS
# %%

# allow us to access it later

# print some of it out

# save them in a file somewhere
