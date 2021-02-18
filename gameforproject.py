from random import randrange
import time
import sys
from os import system, name
from time import sleep

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def end1():
    end = input(""""\n Do you want to play again?
    1: play again
    2: main menu
    3: quit
type a number: """)
    if end == "1":
        duogame()
    elif end == "2":
        menu()
    elif end == "3":
        print("Goodbye!")
        sys.exit()
    else:
        print("Not correct answer, please type a correct number")
        end1()
def info():
    infoinput = input("""Math champions game, produced by Jan Swidzinski 2021
There are two gmamodes: solo, for one player and duo for two players.
Rules are simple there are 5 difficulty levels with 10 questions each.
You have to type in the answer in 5 seconds or less so be fast!

     1. Menu
     
type a number: """)
    if infoinput == "1":
        clear()
        menu()
    else:
        clear()
        print("Not correct answer, please type a correct number\n")
        info()
def setname():
    name1 = input("Player 1 name: ")
    global player1
    player1 = name1
    name2 = input("Player 2 name: ")
    global player2
    player2 = name2
    clear()
def nextplayer():
    input("next turn, 2nd player, are you ready? Press enter to begin")
    clear()
def sologame():
    global points
    level1()
    sleep(1)
    clear()
    level2()
    sleep(1)
    clear()
    level3()
    sleep(1)
    clear()
    level4()
    sleep(1)
    clear()
    level5()
    sleep(1)
    clear()
    print("\nYour final score is:", points)
    input1 = input(""""\nDo you want to play again?
    1: play again
    2: main menu
    3: quit
type a number: """)
    end1()
def duogame():
    global points
    print(player1 + " start!")
    level1()
    points1 = points
    points = 0
    sleep(1)
    clear()
    nextplayer()
    print(player2 + " start!")
    level1()
    points2 = points
    points = points1
    sleep(1)
    clear()
    nextplayer()
    print(player1 + " start!")
    level2()
    points1 = points
    points = points2
    sleep(1)
    clear()
    print(player2 + " start!")
    level2()
    points2 = points
    points = points1
    sleep(1)
    clear()
    print(player1 + " start!")
    level3()
    points1 = points
    points = points2
    sleep(1)
    clear()
    print(player2 + " start!")
    level3()
    points2 = points
    points = points1
    sleep(1)
    clear()
    print(player1 + " start!")
    level4()
    points1 = points
    points = points2
    sleep(1)
    clear()
    print(player2 + " start!")
    level4()
    points2 = points
    points = points1
    sleep(1)
    clear()
    print(player1 + " start!")
    level5()
    points1 = points
    points = points2
    sleep(1)
    clear()
    print(player2 + " start!")
    level5()
    points2 = points
    points = points1
    sleep(1)
    clear()
    print(""+color.BOLD)
    print(color.BOLD + 'Final scores' + color.END)
    print( player1 +":", points1)
    print(player2 + ":", points2)
    print(""+color.BOLD)
    if points1 > points2:
        print(player1 + " wins!"+color.END)
    elif points2 > points1:
        print(player2 + " wins!"+color.END)
    else:
        print(color.RED+ "it's a draw!"+color.END)
    end = input(""""\nDo you want to play again?
    1: play again
    2: main menu
    3: quit
type a number: """)
    end1()

def level1():
    print("Difficulty level 1, You will have ten questions to answer, Let's go!"+color.BOLD)
    t = 0
    global points
    points = 0
    while t < 10:
        if t != 0:
            print(""+color.BOLD)
        a = randrange(2)
        if a == 0:
            i = randrange(1, 10)
            j = randrange(1, 10)
            print(i, "+", j)
            x = i + j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1
            else:
                print("too late")
        elif a == 1:
            i = randrange(1, 10)
            j = randrange(1, 10)
            while i<j:
                i = randrange(1, 10)
                j = randrange(1, 10)
            print(i, "-", j)
            x = i - j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1
            else:
                print("too late")
        t = t + 1
        sleep(1)
        clear()
    if points<0:
        points=0
    print("current points:", points)

def level2():
    print("level 2")
    global points
    t = 0
    while t < 10:
        if t != 0:
            print(""+color.BOLD)
        a = randrange(2)
        if a == 0:
            i = randrange(3, 14)
            j = randrange(20)
            print(i, "+", j)
            x = i + j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1
            else:
                print("too late")
            t = t + 1
        elif a == 1:
            i = randrange(12)
            j = randrange(3, 12)
            print(i, "-", j)
            x = i - j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1
            else:
                print("too late")
            t = t + 1
        sleep(1)
        clear()
    if points < 0:
        points = 0
    print("current points:", points)


def level3():
    print("level 3")
    global points
    t = 0
    while t < 10:
        if t != 0:
            print(""+color.BOLD)
        a = randrange(3)
        if a == 0:
            i = randrange(6, 15)
            j = randrange(2, 12)
            print(i, "*", j)
            x = i * j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1

            else:
                print("too late")
            t = t + 1
        else:
            i = randrange(1, 50)
            j = randrange(2, 25)
            while not i%j ==0 or i==j:
                i = randrange(1, 50)
                j = randrange(2, 25)
            print(i, "/", j)
            x = i / j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                if input1.isdigit():
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("wrong answer! -1")
                    points = points - 1

            else:
                print("too late")
            t = t + 1
        sleep(1)
        clear()
    if points<0:
        points=0
    print("current points:", points)


def level4():
    print("level 4")
    global points
    t = 0
    while t < 10:
        if t != 0:
            print(""+color.BOLD)
        a = randrange(3)
        if a == 0:
            i = randrange(-12, 10)
            j = randrange(-12, 10)
            if i != 1 and j != 1 and i != 0 and j != 0 and i != -1 and j != -1:
                print(i, "*", j)
                x = i * j
                start = time.time()
                input1 = input(color.END+"type in answer: ")
                if time.time() - start < 5:
                    try:
                        int(input1)
                        answer = int(input1)
                        if answer == x:
                            print("good answer! +1")
                            points = points + 1
                        else:
                            print("wrong answer! -1")
                            points = points - 1
                    except ValueError:
                        print("wrong answer! -1")
                        points = points - 1

                else:
                    print("too late")
                t = t + 1
        else:
            i = randrange(-51, 51)
            j = randrange(-11, 11)
            while i==0 or j==0 or not i%j ==0:
                i = randrange(-51, 51)
                j = randrange(-11, 11)
            print(i, "/", j)
            x = i / j
            start = time.time()
            input1 = input(color.END+"type in answer: ")
            if time.time() - start < 5:
                try:
                    int(input1)
                    answer = int(input1)
                    if answer == x:
                        print("good answer! +1")
                        points = points + 1
                    else:
                        print("wrong answer! -1")
                        points = points - 1
                except ValueError:
                    print("wrong answer! -1")
                    points = points - 1

            else:
                print("too late")
            t = t + 1
        sleep(1)
        clear()
    if points<0:
        points=0
    print("current points:", points)


def level5():
    print("level 5")
    global points
    t = 0
    while t < 10:
        if t != 0:
            print(""+color.BOLD)
        a = randrange(4)
        if a == 0:
            i = randrange(-9, 6)
            j = randrange(-9, 6)
            k = randrange(-11, 11)
            if i != 1 and j != 1 and i != 0 and j != 0 and i != -1 and j != -1 and i % j == 0:
                print(i, "/", j, "-", k)
                x = i / j - k
                start = time.time()
                input1 = input(color.END+"type in answer: ")
                if time.time() - start < 5:
                    try:
                        int(input1)
                        answer = int(input1)
                        if answer == x:
                            print("good answer! +1")
                            points = points + 1
                        else:
                            print("wrong answer! -1")
                            points = points - 1
                    except ValueError:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("too late")
                t = t + 1
        elif a == 1:
            i = randrange(-31, 31)
            j = randrange(-11, 11)
            k = randrange(-11, 11)
            if i != j and i != 0 and j != 0 and i != -1 and j != -1 and i % j == 0:
                print(i, "/", j, "+", k)
                x = i / j + k
                start = time.time()
                input1 = input(color.END+"type in answer: ")
                if time.time() - start < 5:
                    try:
                        int(input1)
                        answer = int(input1)
                        if answer == x:
                            print("good answer! +1")
                            points = points + 1
                        else:
                            print("wrong answer! -1")
                            points = points - 1
                    except ValueError:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("too late")
                t = t + 1
        elif a == 2:
            i = randrange(-11, 11)
            j = randrange(-11, 11)
            k = randrange(-11, 11)
            if i != j and i != 0 and j != 0 and i != -1 and j != -1 and i % j == 0:
                print(i, "*", j, "+", k)
                x = i * j + k
                start = time.time()
                input1 = input(color.END+"type in answer: ")
                if time.time() - start < 5:
                    try:
                        int(input1)
                        answer = int(input1)
                        if answer == x:
                            print("good answer! +1")
                            points = points + 1
                        else:
                            print("wrong answer! -1")
                            points = points - 1
                    except ValueError:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("too late")
                t = t + 1
        elif a == 3:
            i = randrange(-11, 11)
            j = randrange(-11, 11)
            k = randrange(-11, 11)
            if i != j and i != 0 and j != 0 and i != -1 and j != -1 and i % j == 0:
                print(i, "*", j, "+", k)
                x = i * j + k
                start = time.time()
                input1 = input(color.END+"type in answer: ")
                if time.time() - start < 5:
                    try:
                        int(input1)
                        answer = int(input1)
                        if answer == x:
                            print("good answer! +1")
                            points = points + 1
                        else:
                            print("wrong answer! -1")
                            points = points - 1
                    except ValueError:
                        print("wrong answer! -1")
                        points = points - 1
                else:
                    print("too late")
                t = t + 1
        sleep(1)
        clear()
    if points<0:
        points=0
    print("current points:", points)


def menu():
    global answer
    answer = False
    global duo
    global solo
    solo = False
    duo = False
    print(""+color.BOLD)
    print(color.BOLD + 'Welcome to math Champions game!\n' + color.END)
    beginning = input("""Here you can sharpen up your math skills or play against someone
    1: play game
    2: info
    3: quit

type a number: """)
    if beginning == "1":
        while answer == False:
            solo_duo = input("""\nDo you want to play solo or duo?
    1: solo
    2: duo 
type a number: """)
            if solo_duo == "1":
                clear()
                sologame()
                answer = True
            elif solo_duo == "2":
                clear()
                setname()
                duogame()
                answer = True
            else:
                print("Not correct answer, please type a correct number")
    elif beginning == "2":
        clear()
        info()
    elif beginning == "3":
        clear()
        print("Goodbye!")
        sys.exit
    else:
        clear()
        print("Not correct answer, please type a correct number")
        menu()

menu()



# add different gamemodes
# delete lines after going to main and info etc.
# add ability to add custom names
# try to make class out of levels
