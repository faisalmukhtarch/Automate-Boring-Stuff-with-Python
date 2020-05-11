import random
ran = random.choice(('ROCK', 'PAPER', 'SCISSORS'))
print("ROCK, PAPER, SCISSORS" )
win = 0
lose = 0
tie = 0
print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
guess = str(input())
print(ran + " versus...")
while True:
    if guess == "r":
        print("ROCK")
        if ran == "ROCK":
            print("Its a tie")
            tie = tie + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "PAPER":
            print("You Lose")
            lose = lose + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "SCISSORS":
            print("You Win!")
            win = win + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
    elif guess == "p":
        print("PAPER")
        if ran == "PAPER":
            print("Its a tie")
            tie = tie + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "SCISSORS":
            print("You Lose")
            lose = lose + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "ROCK":
            print("You Win!")
            win = win + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
    elif guess == "s":
        print("SCISSORS")
        if ran == "SCISSORS":
            print("Its a tie")
            tie = tie + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "ROCK":
            print("You Lose")
            lose = lose + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
        elif ran == "PAPER":
            print("You Win!")
            win = win + 1
            print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
    elif guess == "q":
        print("Exit")