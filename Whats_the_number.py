import random


class User:
    # ask user for name and age
    User_name = input("What is your name? ")
    User_age = int(input("What is your age? "))

    def __init__(self, name, age):
        self.name = self.User_name
        self.age = self.User_age


class Number:
    # collect users random number and return a value to the user based on their selection

    def __init__(self):
        Random_number = int(input("Pick a number between 1 -10?"))
        self.number = Random_number

    def value(self):
        number_value = int(random.randint(0, 10))
        if self.number == number_value:
            print("You're answer is correct")
        elif self.number < number_value:
            print(f"Great guess {User.User_name}, the number is {number_value} and you were down by " + str(number_value - self.number))
        else:
            print(f"Good guess {User.User_name}, the number is {number_value} and you were up by " + str(self.number - number_value))


if __name__ == '__main__':
    number_guess = Number()
    number_guess.value()
