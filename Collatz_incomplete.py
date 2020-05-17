number = 0
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number
    else:
        print(3 * number + 1)
        return number

def test():
    while True:
        try:
            print("Enter number: ")
            number = int(input())
            if collatz(number):
                return 1
                break
            else:
                collatz(number) * number
        except ValueError:
            print("Please enter integer only")
test()
