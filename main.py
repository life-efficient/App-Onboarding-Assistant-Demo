# %%
import json
import pandas as pd
# APP ONBOARDING ASSISTANT

# take user input
# age = input("What's your age?")
# username = input("What's your username?")
# location = input("What's your location?")


def get_and_validate_user_attribute(attribute_name):
    confirmation = None
    while confirmation != "Y":
        value = input(f"What's your {attribute_name}?")
        print(f"Can you confirm that your {attribute_name} is {value}?")
        confirmation = input("Enter Y/N\n")
    print("All good, let's move on")
    return value


class User:
    def __init__(self, name, age):  # remove need to call this manually
        self.data = {
            "age": age,
            "name": name
        }

    def __repr__(self, prefix=None):  # print the user nicely
        return f"Hey! My name is {self.data['name']}. I am {self.data['age']} years old"

    def update(self, attribute_name: str, value: any):
        """Updates a attribute of this instance of the class by name

        if the parameter is equal to "name", then self.name will be set to value
        if the parameter is equal to "age", then self.age will be set to value

        Parameters:
        - attribute_name: str
        - value: any

        Returns: None
        """
        if attribute_name not in self.data.keys():
            raise ValueError("That's not a valid piece of data to update")
        self.data[attribute_name] = value

    # TODO save to file
    def save(self):
        with open("userdata.json", "w") as file:
            json.dump(self.data, file)

            # file.write(self.name)

    def load(self):
        """load from file"""
        with open("userdata.json", "r") as file:
            user_data = json.load(file)
            self.data = user_data

    # TODO (using static method - warning - more advanced)


# %%
def ask_login_or_signup():
    # TODO def function to ask whether login or signup
    choice = input("Do you want to log in (L) or sign up (S)?")
    try:
        assert choice in [
            "S", "L"], f'Option needs to be one of log in (L) or sign up (S). You gave "{choice}"'
    except AssertionError as e:
        print(type(e))
        print(e)
        # print
        choice = ask_login_or_signup()
    return choice


max_attempts = 3


def login(attempts=0):  # create login function

    username = input("Username: ")  # request username
    password = input("Password: ")  # request password
    df = pd.read_json("userdata.json")
    df = df.set_index("username")

    # VALIDATE USERNAME
    if username not in df.index.values:
        print("User not found. Please try again...")
        return login(attempts=attempts)

    # VALIDATE PASSWORD
    record = df.loc[username]
    if record["password"] == password:  # validate password
        print("Login successful")
        return User(record["name"], record["age"])  # create user instance
    else:
        attempts += 1
        if attempts == max_attempts:
            raise Exception("Too many attempts")
        print(
            f"Incorrect login credentials, {max_attempts - attempts} attempts remaining. Please try again...")
        return login(attempts=attempts)


def main():

    choice = ask_login_or_signup()
    if choice == "L":
        login()
    elif choice == "S":
        sign_up()
    else:
        raise Exception
    # user = User("harry", 25)
    # print(user.__repr__())
    # print(user)

    # GET AND VALIDATE USER ATTRIBUTES
    # name = get_and_validate_user_attribute("name")
    # age = get_and_validate_user_attribute("age")

    # print(user.data["age"])
    # print(user.age)
    # user.update("agecsdcds", 26)
    # print(user.age)
    # TODO create loop to continually ask user what action they want to take

    # ask use to login or signup


    # %%
main()
