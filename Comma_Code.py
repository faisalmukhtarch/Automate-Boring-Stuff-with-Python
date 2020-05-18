spam = ['apple', 'banana', 'kids', 'cats', 'something', 'good']


def seprator(spam):
    print(", ".join(spam[:-1]) + " and " + spam[-1])

seprator(spam)