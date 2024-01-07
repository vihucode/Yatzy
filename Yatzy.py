"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Vili Huotari

Program for yatzy game in window.
"""
#Global variable is used for keep on track players turns
TURN = 0

# List of possible scoring choices in game
SCORING_SECTION = [
    "Ones",
    "Twos",
    "Threes",
    "Fours",
    "Fives",
    "Sixes",
    "One Pair",
    "Two Pairs",
    "Three Of a Kind",
    "Four Of a Kind",
    "Small Straight",
    "Large Straight",
    "Full House",
    "Chance",
    "Yatzy"
]
from tkinter import *
import random

class Yatzy:
    """
    Class for players information control:
        names,
        points,
        turn rolls,
        own scoreboard.
    """

    def __init__(self, name):
        """
        Constructor makes players informations.
        :param name: str, Name of the player
        """
        self.__player = name
        self.__player_points = 0
        self.__rolls = 0
        self.__scoring_system = {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "One Pair": -1,
            "Two Pairs": -1,
            "Three Of a Kind": -1,
            "Four Of a Kind": -1,
            "Small Straight": -1,
            "Large Straight": -1,
            "Full House": -1,
            "Chance": -1,
            "Yatzy": -1
        }

    def __str__(self):
        """
        :return: str, player name
        """
        return self.__player

    def get_points(self):
        """
        :return: int, player points
        """
        return self.__player_points

    def get_rolls(self):
        """
        :return: int, player roll count
        """
        return self.__rolls

    def add_points(self, score):
        """
        Add specific amout of points after turn in game.
        :param score: int, player score after turn
        """
        self.__player_points += score

    def score(self, score, choice):
        """
        Method add score to right place in player own scoreboard. If score is
        over zero then method adds score if not then adds one point. One point is added
        because then program can see different between used choice and unused.
        :param score: int, player score from turn
        :param choice: str, score choice that he/she used on turn
        """
        if score > 0:
            self.__scoring_system[choice] += (score + 1)
        else:
            self.__scoring_system[choice] += 1

    def return_score(self, choice):
        """
        Returns choices points from scoreboard options.
        :param choice: str, score choice that he/she used on turn
        :return: int, points of specifis score
        """
        return self.__scoring_system[choice]

    def return_scoring_system(self):
        """
        :return: list, returns list of the player scoreboard
        """
        return self.__scoring_system

    def add_rolls(self):
        """
        Adds roll to players rolls after he/she used one.
        """
        self.__rolls += 1

    def zero_rolls(self):
        """
        Erase all rolls after player turn.
        """
        self.__rolls = 0

    def whipe_scoreboard(self):
        """
        Whipe all points fromm scoreboard back to begining values after game.
        """
        for choice in self.__scoring_system:
            self.__scoring_system[choice] = -1

    def score_situtiation(self):
        """
        Method go through player scoreboard if all score options is already used. If not then returns
        False and player game will continue if all are used then returns True. After all players returns
        True game ends. Method also checks if player gets enough points for bonus points and if gets then
        adds points for player.
        :return: boolean, True if all options used or False if not
        """

        bonus_score = 0
        numbers = 0
        for score in self.__scoring_system:
            number = self.__scoring_system[score]
            if number == -1:
                return False
            elif numbers <= 5 and self.__scoring_system[score] > 0:
                bonus_score += self.__scoring_system[score]
            numbers += 1

        if bonus_score >= 63:
            self.__player_points += 50

        return True

def gamewindow():
    """
    Main function for game window funktions.
    """

    game = Tk()
    game.geometry("600x500")
    game.title("Yatzy")

    #List of players
    players = []

    #Dict for five dices and values.
    dices_numbers = {
        "dice_1": 0,
        "dice_2": 0,
        "dice_3": 0,
        "dice_4": 0,
        "dice_5": 0
    }

    #Images

    dice1 = PhotoImage(file="yksi.png")
    dice2 = PhotoImage(file="kaksi.png")
    dice3 = PhotoImage(file="kolme.png")
    dice4 = PhotoImage(file="nelja.png")
    dice5 = PhotoImage(file="viisi.png")
    dice6 = PhotoImage(file="kuusi.png")
    bg = PhotoImage(file="bg.png")

    #CANVAS

    background = Canvas(game, width=600, height=500)
    background.pack(fill="both", expand=True)

    background.create_image(0,0,image=bg, anchor="nw")

    #PLAYER NAMES AND POINTS LABELS

    player = background.create_text(85,150,text="", font=("Helvetica", 10), fill="white")
    player_points = background.create_text(85,170,text="", font=("Helvetica", 10), fill="white")

    player1 = background.create_text(85,200,text="", font=("Helvetica", 10), fill="white")
    player1_points = background.create_text(85,220,text="", font=("Helvetica", 10), fill="white")

    player2 = background.create_text(85,250,text="", font=("Helvetica", 10), fill="white")
    player2_points = background.create_text(85,270,text="", font=("Helvetica", 10), fill="white")

    player3 = background.create_text(85,300,text="", font=("Helvetica", 10), fill="white")
    player3_points = background.create_text(85,320,text="", font=("Helvetica", 10), fill="white")

    #TEXT LABELS

    welcome_text = background.create_text(275,25,text="WELCOME TO THE YATZY!", font=("Helvetica", 10), fill="white")
    rules = background.create_text(275,115,text="\n\n\n\n\n\n\nRULES:\nPlayer have 3 rolls during the turn.\n"
                                                "When player is satisfied with the dices numbers\n"
                                                "player chooses score from scoreboard.\n"
                                                "After that turn change. Game ends when\n"
                                                "all players scoreboards are full. Winner\n"
                                                "is the one with the most points.",
                                                font=("Helvetica", 10), fill="white", justify="center")

    player1_name = background.create_text(95,75,text="Enter 1-4 player names.\n(Matti,Teppo...)",
                                          font=("Helvetica", 10), fill="white")

    scoring_system_board = background.create_text(294,285,text="",
                                                  font=("Helvetica", 10), fill="white", justify="left")

    #ENTRY FOR NAMES

    players_names = Entry()
    players_names_window = background.create_window(25, 100, anchor="nw", window=players_names)

    #START BUTTON

    start_game = Button(game, text="Start Game", command=lambda: player_names(players_names.get()))
    start_game_window = background.create_window(235, 50, anchor="nw", window=start_game)

    #EXIT BUTTON

    exit_game = Button(game, text="Exit game", command=lambda: close_game(), bg="red")
    exit_game_window = background.create_window(475,400, anchor="nw", window=exit_game)


    def player_names(names):
        """
        Function go throug given player names and separetes them from eachother to list.
        Creates players for class and then starts gamedepending on how many players were
        given. Funktion also disables start button and makesure that players scoreboards
        are in starting values. Lastly starts the game section.
        :param names: str, string of names
        """
        global TURN

        #Check that name is not empty if is then return and print text
        if names == "":
            background.itemconfig(rules, text=f"Give player name!", fill="white")
            return

        start_game['state'] = DISABLED

        #If played again this section delete last game players and points
        if len(players) > 0:
            erase_players()
            player = 0
            while player < len(players):
                players.pop(player)

        #Change turn back to zero
        TURN = 0

        #Separetes names from string to list
        name_list = names.split(",")
        for name in name_list:
            name = name.strip()
            name = Yatzy(f"{name}")
            players.append(name)

        #Checks how many players and calls right function
        if len(name_list) == 1:
            solo()
        elif len(name_list) == 2:
            duo()
        elif len(name_list) == 3:
            trio()
        else:
            quads()

        #Whipes players scoreboard one at the time
        player_number = 0
        while player_number < len(players):
            players[player_number].whipe_scoreboard()
            player_number += 1

        start()

    def erase_players():
        """
        Erase player stats if played again after match.
        """
        background.itemconfig(player, text=f"")
        background.itemconfig(player_points, text=f"")

        background.itemconfig(player1, text=f"")
        background.itemconfig(player1_points, text=f"")

        background.itemconfig(player2, text=f"")
        background.itemconfig(player2_points, text=f"")

        background.itemconfig(player3, text=f"")
        background.itemconfig(player3_points, text=f"")


    def solo():
        """
        Function creates text labels of name and points on canvas.
        :param name: str, name of the player
        """
        background.itemconfig(player, text=f"{players[0]}")
        background.itemconfig(player_points, text=f"0")


    def duo():
        """
        Function creates text labels of names and points on canvas.
        """
        background.itemconfig(player, text=f"{players[0]}")
        background.itemconfig(player_points, text=f"0")

        background.itemconfig(player1, text=f"{players[1]}")
        background.itemconfig(player1_points, text=f"0")


    def trio():
        """
        Function creates text labels of names and points on canvas.
        """
        background.itemconfig(player, text=f"{players[0]}")
        background.itemconfig(player_points, text=f"0")

        background.itemconfig(player1, text=f"{players[1]}")
        background.itemconfig(player1_points, text=f"0")

        background.itemconfig(player2, text=f"{players[2]}")
        background.itemconfig(player2_points, text=f"0")


    def quads():
        """
        Function creates text labels of names and points on canvas.
        """

        background.itemconfig(player, text=f"{players[0]}")
        background.itemconfig(player_points, text=f"0")

        background.itemconfig(player1, text=f"{players[1]}")
        background.itemconfig(player1_points, text=f"0")

        background.itemconfig(player2, text=f"{players[2]}")
        background.itemconfig(player2_points, text=f"0")

        background.itemconfig(player3, text=f"{players[3]}")
        background.itemconfig(player3_points, text=f"0")


    def start():
        """
        Funktion for ingame funktions.
        """

        def dices(buttons):
            """
            Function for dices. Function includes list of dices images variables and dices
            names for creating dices ímages with random values on the canvas. Function also changes dices hold
            buttons back to enabled after roll.
            :param buttons: list, list of buttons variables to know which ones are on hold.
            """

            #List of the dices images
            dices_list = [
                dice1,
                dice2,
                dice3,
                dice4,
                dice5,
                dice6
            ]

            #List of dices names
            dices = [
                "dice_1",
                "dice_2",
                "dice_3",
                "dice_4",
                "dice_5"
            ]

            #New list of random dice images
            random_dices = []
            #New list of random dice values
            random_numbers = []

            #This section randomize dices values and images and adds
            #those to lists above.
            dice_count = 1
            while dice_count <= 5:
                dice = random.randint(0, 5)
                random_numbers.append((dice + 1))
                random_dices.append(dices_list[dice])
                dice_count += 1

            #This section creates images to the canvas from above
            #randomized lists of values. Image will be changed if
            #state button of that image is normal. Else image will
            #be the same as last roll.
            count = 0
            y = 90
            while count <= 4:
                dice = dices[count]
                if buttons[count]['state'] == NORMAL or players[TURN].get_rolls() == 0:
                    dices_numbers[dice] = random_numbers[count]
                    dice_pic = background.create_image(530, y, image=random_dices[count])
                count += 1
                y += 50

            #Changes all buttons state back to normal after roll.
            hold_dice1['state'] = NORMAL
            hold_dice2['state'] = NORMAL
            hold_dice3['state'] = NORMAL
            hold_dice4['state'] = NORMAL
            hold_dice5['state'] = NORMAL

            play_game()


        def score_choice(choice):
            """
            Function calculate correct amount of points for player depending on
            which choice player has been chosen and call "add_points" method to
            add points to correct player. Function also set ingame buttons 'state'
            to normal after turn and moves turn to next player.

            :param choice:
            :return:
            """
            global TURN

            #List of dices names
            dices = [
                "dice_1",
                "dice_2",
                "dice_3",
                "dice_4",
                "dice_5"
            ]
            #List of values count. List starts from biggest to calculate
            #always the biggest sum of points for player.
            numbers_count = {
                6 : 0,
                5 : 0,
                4 : 0,
                3 : 0,
                2 : 0,
                1 : 0
            }

            #Keeps optionmenu button text the same
            clicked.set("Score list")

            #Check if player has already used this score choice and returns back to choose again.
            choice_score = players[TURN].return_score(choice)
            if choice_score >= 0:
                background.itemconfig(rules, text=f"You have already used this choice!")
                return



            #Finds choice from scoring list
            selection = int(SCORING_SECTION.index(choice))

            #First section calculates points for sum of same numbers values of 1 to 6
            #depending what player has chosen. Rest of the section calculates points
            #in different choices player make.
            score = 0
            if selection <= 5:
                for dice in dices:
                    number = dices_numbers[dice]
                    if number == (selection + 1):
                        score += (selection + 1)
            #ONE PAIR
            elif selection == 6:
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count >= 2:
                        score += (number2 * 2)
                        break
            #TWO PAIRS
            elif selection == 7:
                two_pairs = 0
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count >= 2:
                        score += (number2 * 2)
                        two_pairs += 1
                if two_pairs < 2:
                    score = 0
            #THREE OF A KIND
            elif selection == 8:
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count >= 3:
                        score += (number2 * 3)
                        break
            #FOUR OF A KIND
            elif selection == 9:
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count >= 4:
                        score += (number2 * 4)
                        break
            #SMALL STRAIGHT
            elif selection == 10:
                straight = "12345"
                for dice in dices:
                    number1 = dices_numbers[dice]
                    if str(number1) in straight and straight != "":
                        straight = straight.replace(f"{str(number1)}", "")
                        if straight == "":
                            score += 15
            #LARGE STRAIGHT
            elif selection == 11:
                straight = "23456"
                for dice in dices:
                    number1 = dices_numbers[dice]
                    if str(number1) in straight and straight != "":
                        straight = straight.replace(f"{str(number1)}", "")
                        if straight == "":
                            score += 20
            #FULL HOUSE
            elif selection == 12:
                full_house = ""
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count == 2:
                        score += (number2 * 2)
                        full_house += "1"
                    elif count == 3:
                        score += (number2 * 3)
                        full_house += "2"
                if full_house != "21" and full_house != "12":
                    score = 0
            #CHANCE
            elif selection == 13:
                for dice in dices:
                    number1 = dices_numbers[dice]
                    score += number1
            #YATZY
            elif selection == 14:
                for dice in dices:
                    number1 = dices_numbers[dice]
                    numbers_count[number1] += 1
                for number2 in numbers_count:
                    count = numbers_count[number2]
                    if count == 5:
                        score += 50
                        break

            #Check if player get points or not.
            if score > 0:
                players[TURN].add_points(score)
            else:
                score -= 1

            #Call function to add points to scoreboard
            players[TURN].score(score, choice)

            #Call function to update player points label
            update_points()

            #Change ingame button right 'state' after turn
            hold_dice1['state'] = NORMAL
            hold_dice2['state'] = NORMAL
            hold_dice3['state'] = NORMAL
            hold_dice4['state'] = NORMAL
            hold_dice5['state'] = NORMAL
            selections['state'] = DISABLED
            roll_button['state'] = NORMAL

            #Erase player rolls
            players[TURN].zero_rolls()

            #If game not ended then moves turn to next player and
            #updates game progress label.Lastly updates scoreboard to right player
            if game_end() == False:
                if TURN < 1 and len(players) == 2:
                    TURN += 1
                elif TURN < 2 and len(players) == 3:
                    TURN += 1
                elif TURN < 3 and len(players) == 4:
                    TURN += 1
                else:
                    TURN = 0
                background.itemconfig(rules, text=f"Player {players[TURN]} turn", fill="white")

                scoreboard_update()

            #Disables buttons before next player roll dices
            if players[TURN].get_rolls() == 0:
                hold_dice1['state'] = DISABLED
                hold_dice2['state'] = DISABLED
                hold_dice3['state'] = DISABLED
                hold_dice4['state'] = DISABLED
                hold_dice5['state'] = DISABLED
                selections['state'] = DISABLED

        def play_game():
            """
            Funktion count players rolls when its their turn. After 3 rolls funktion call
            "zero_rolls" and erases all rolls ready for the next turn.
            """
            global TURN

            #Changes score selection menu to normal state after use
            selections['state'] = NORMAL

            #Keep on eye how many rolls is used and add/erases rolls. Also changes roll
            #buttons state disabled if all player rolls are used.

            if players[TURN].get_rolls() % 2 != 0 or players[TURN].get_rolls() == 0:
                players[TURN].add_rolls()
            else:
                players[TURN].zero_rolls()
                roll_button['state'] = DISABLED

            #Changes rules text to track players turns in game so players sees hows turn it is.
            background.itemconfig(rules, text=f"Player {players[TURN]} turn", fill="white")

            scoreboard_update()

        def scoreboard_update(winner=-1):
            """
            Funktion create and update player own scoreboard system. Also checks if game is end.
            If it is then prints and update winner scoreboard. If not then prints scoreboard
            whos turn it is.

            :param winner: int, if game ends value is winners place number in list "players"
            """

            #Checks if game is ended or not
            if winner != -1:
                player_name = players[winner]
            else:
                player_name = players[TURN]

            score_list = player_name.return_scoring_system()

            #Creates title for scoreboard. Scoreboard will be added under this.
            text = f"--- {player_name}'s Scoreboard ---\n"

            #This section go throuh player own scoreboard. Adds choices and values to srting "text".
            #If value if under zero which means it it unused then prints blank for that.
            for choice in score_list:
                if score_list[choice] < 0:
                    score = "    "
                else:
                    score = score_list[choice]

                if len(str(score_list[choice])) == 2:
                    text += f"     | {score} |      {choice} \n"
                else:
                    text += f"     |  {score}  |      {choice} \n"

            #Update scoreboard label for right scoreboard
            background.itemconfig(scoring_system_board,text=f"{text}")

        def update_points():
            """
            Function updates players points after their turns.
            """
            if TURN == 0:
                background.itemconfig(player_points, text=f"{players[TURN].get_points()}")
            elif TURN == 1:
                background.itemconfig(player1_points, text=f"{players[TURN].get_points()}")
            elif TURN == 2:
                background.itemconfig(player2_points, text=f"{players[TURN].get_points()}")
            else:
                background.itemconfig(player3_points, text=f"{players[TURN].get_points()}")

        def game_end():
            """
            Function firstly check if all players have used all their score options.
            If not then game continues normaly and return False. If is then return True and
            funktion disables all ingame buttons. Then go trough all players scores and stores
            the highest scores and player(s) number(s).Prints winner text and winner scoreboard. Lastly
            :return boolean, Return True or False depending if game contiues or not.
            """

            #Go throug players scoreboards and add one to "full_choices" if full
            full_choices = 0
            next = 0
            while next < len(players):
                full = players[next].score_situtiation()
                if full == True:
                    full_choices += 1
                next += 1

            scoreboard_update()

            #If all players scoreboards are full then disables buttons
            if full_choices == len(players):
                hold_dice1['state'] = DISABLED
                hold_dice2['state'] = DISABLED
                hold_dice3['state'] = DISABLED
                hold_dice4['state'] = DISABLED
                hold_dice5['state'] = DISABLED
                roll_button['state'] = DISABLED
                selections['state'] = DISABLED

                #If game was solo then prints text below
                tie_list = []
                if len(players) == 1:
                    final_score = players[TURN].get_points()
                    background.itemconfig(rules, text=f"     You get {final_score} points!\n"
                                                      f"     Enter names and press 'Start Game' button\n"
                                                      f"     if you want new game.")

                #if there is many players then goes throug players score and
                #after the winner is clear then prints text below and winner scoreboard.
                elif len(players) > 1:
                    player_count = 0
                    winner = 0
                    final_score = 0
                    while player_count < len(players):
                        score = players[player_count].get_points()
                        if score > final_score:
                            winner = player_count
                            final_score = score
                        elif score == final_score:
                            if winner not in tie_list and winner != player_count:
                                tie_list.append(winner)
                            tie_list.append(player_count)
                        player_count += 1
                    if len(tie_list) < 1:
                        background.itemconfig(rules, text=f"      {players[winner]} wins with {final_score} points!\n"
                                                          f"      Enter names and press 'Start Game' button if\n"
                                                          f"      you want new game.")
                    else:
                        winners = ""
                        for player in tie_list:
                            winners += f" {players[player]},"
                            background.itemconfig(rules, text=f"      {winners} wins with {final_score} points!\n"
                                                              f"      Enter names and press 'Start Game' button if\n"
                                                              f"      you want new game.")
                    scoreboard_update(winner)

                #Enables start game button for new game
                start_game['state'] = NORMAL

                return True

            else:
                return False

        #Sets correct text for optionmenu
        clicked = StringVar(game)
        clicked.set("Score list")

        #OPTIONMENU BUTTON

        selections = OptionMenu(game, clicked, *SCORING_SECTION, command= score_choice)
        selections_window = background.create_window(350, 50, anchor="nw", window=selections)

        #INGAME BUTTONS

        roll_button = Button(game, text="Roll", command=lambda: dices(buttons))
        hold_dice1 = Button(game, text="Dice 1", command=lambda: disable(hold_dice1))
        hold_dice2 = Button(game, text="Dice 2", command=lambda: disable(hold_dice2))
        hold_dice3 = Button(game, text="Dice 3", command=lambda: disable(hold_dice3))
        hold_dice4 = Button(game, text="Dice 4", command=lambda: disable(hold_dice4))
        hold_dice5 = Button(game, text="Dice 5", command=lambda: disable(hold_dice5))

        background.create_window(450, 55, anchor="nw", window=roll_button)
        background.create_window(420, 85, anchor="nw", window=hold_dice1)
        background.create_window(420, 135, anchor="nw", window=hold_dice2)
        background.create_window(420, 185, anchor="nw", window=hold_dice3)
        background.create_window(420, 235, anchor="nw", window=hold_dice4)
        background.create_window(420, 285, anchor="nw", window=hold_dice5)

        #Disable selections before first player roll dices
        selections['state'] = DISABLED
        hold_dice1['state'] = DISABLED
        hold_dice2['state'] = DISABLED
        hold_dice3['state'] = DISABLED
        hold_dice4['state'] = DISABLED
        hold_dice5['state'] = DISABLED

        #List of dice hold buttons variables names
        buttons = [
            hold_dice1,
            hold_dice2,
            hold_dice3,
            hold_dice4,
            hold_dice5
        ]

        background.itemconfig(rules, text=f"Player {players[TURN]} turn", fill="white")

        def disable(button):
            """
            Disabled given button.
            :param button: variable, name of the button variable
            """
            button['state'] = DISABLED

    def close_game():
        """
        Closes the game window.
        """
        game.destroy()

    game.mainloop()

def main():
    gamewindow()

if __name__ == "__main__":
    main()
