import random


def generate(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res


def score(goal, testString):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numSame = numSame + 1
    return numSame/len(goal) * 100


def main():
    goalString = "methinks it is like a weasel"
    newString = generate(28)
    iterations = 0
    bestScore = 0
    bestString = ""
    while score(goalString, newString) < 100:
        newString = generate(28)
        if score(goalString, newString) > bestScore:
            bestScore = score(goalString, newString)
            bestString = newString
        iterations = iterations + 1
        if iterations % 100000 == 0:
            print("Best score is %s with the string generated as (%s)" %
                  (str(bestScore), bestString))
    print("String matched after %d tries." % iterations)


main()
