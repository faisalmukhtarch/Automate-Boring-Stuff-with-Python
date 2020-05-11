import random
i = random.randint(0, 10)
print("I am thinking of a number between 1 and 10")
while i in range(10):
    print("Take a guess")
    guess = int(input())
    if guess < i:
        print("Too low")
    elif guess > i:
        print("Too High")
    elif guess == i:
        print("Great Job, you guessed my number " + str(i))
    break