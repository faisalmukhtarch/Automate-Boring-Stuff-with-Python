import random
ran = random.choice(('ROCK', 'PAPER', 'SCISSORS'))
print("ROCK, PAPER, SCISSORS" )
win = 0
lose = 0
tie = 0
score = print(str(win) + " Wins " + str(lose) + " Losses " + str(tie) + " Ties")
print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
guess = str(input())
print(ran + " versus...")
if guess == "r":
    print("ROCK")
    if ran == "ROCK":
        print("Its a tie")
        tie = tie + 1
        print(score)
    elif ran == "PAPER":
        print("You Lose")
        lose = lose + 1
        print(score)
    elif ran == "SCISSORS":
        print("You Win!")
        win = win + 1
        print(score)
elif guess == "p":
    print("PAPER")
elif guess == "s":
    print("SCISSORS")
elif guess("q"):
    print("Exit")