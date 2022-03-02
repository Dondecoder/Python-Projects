import random
import sys

class User:
    # ask user for name
    def __init__(self, name):
        self.name = User_name


class Results:
    # record user input
    def __init__(self):
        self.user_input = input("Pick rock, paper, or scissors?")

        self.selection = self.user_input

    def output(self):
        # return cpu output and run through the game
        self.selection = self.user_input
        cpu_output = random.choice(("rock", "paper", "scissors"))

        if self.selection == cpu_output:
            print(f"{User_name} I chose {cpu_output} it looks like we're tied")
        elif self.selection == "rock" or " rock" or " rock ":
            if cpu_output == "paper":
                print(f"I chose {cpu_output}. Paper beats rock. {User_name} it looks like I won this round")
            else:
                print(f"Great job {User_name}. Rock beats scissors it looks like you won this round")
        elif self.selection == "paper" or " paper" or " paper ":
            if cpu_output == "scissors":
                print(f"Scissors beats paper. {User_name} it looks like I won this round")
            else:
                print(f"Great job {User_name}. Paper beats rock it looks like you won this round")
        elif self.selection == "scissors" or " scissors" or " scissors ":
            if cpu_output == "rock":
                print(f"Rock beats scissors. {User_name} it looks like I won this round")
            else:
                print(f"Great job {User_name}. Scissors beats paper it looks like you won this round")

    def restart(self):
        # allow user to restart the game
            while True:
                game_reset = str.lower(input("Would you like to play again?"))
                if game_reset == "yes" or " yes" or " yes ":
                    print(f"Starting up a new game {User_name}")
                    rps_game.__init__()
                    rps_game.output()


                else:
                    print(f"Exiting the game. Thanks for playing {User_name}")
                    sys.exit()


User_name = input("What is your name? ")

while True:
    if __name__ == '__main__':
        rps_game = Results()
        rps_game.output()
        rps_game.restart()

