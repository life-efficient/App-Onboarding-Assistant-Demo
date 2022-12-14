# %%
import json
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

    def print_nicely(self, prefix=None):  # print the user nicely
        print(
            f"Hey! My name is {self.data.name}. I am {self.data.age} years old")

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


def main():

    # GET AND VALIDATE USER ATTRIBUTES
    # name = get_and_validate_user_attribute("name")
    # age = get_and_validate_user_attribute("age")

    # TODO 1 pass user attributes to user class to initialise new user

    print(user.data["age"])
    # print(user.age)
    # user.update("agecsdcds", 26)
    # print(user.age)
    # TODO create loop to continually ask user what action they want to take
    # TODO create signup method
    # TODO create login method


# %%
