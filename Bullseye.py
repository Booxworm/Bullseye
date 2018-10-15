from random import shuffle

def genDistinct():
    numList = list(map(str,range(0,10)))                # List from 0 - 9
    shuffle(numList)                                    # Shuffles List
    num = ''.join(numList[:4])                          # Generates 4 digit number
    return num

def getInput(allowRepeat=False):
    # Get user input
    try:
        number = input("Enter a 4-digit number, with distinct digits (#### to leave): ")
        # Checks for control variable
        if number == '####':
            print("You have decided to leave...")
        # Checks for length and if its a number
        elif len(number) != 4 or not number.isdigit():
            raise Exception()
        else:
            # Checks for distinct values
            if not allowRepeat:
                numList = []
                for digit in number:
                    numList.append(digit)
                if len(numList) != len(set(numList)):
                    raise Exception()

        return number
    except:
        print("That is not a unique 4-digit number!\n")
        return False


def checkGuess(guess, number):
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] in number:
            if guess[i] == number[i]: bulls += 1        # Same number, same index
            else: cows += 1                             # Same number, different index
    return(cows, bulls)

def userGuess():
    # Game loop
    guessing = True
    number = genDistinct()
    while guessing:
        guess = getInput(allowRepeat=True)
        if guess == '####': break
        elif not guess: continue
        # Check users guess
        bullseye = checkGuess(guess, number)
        print("You found {} cows and {} bulls!".format(bullseye[0], bullseye[1]))
        if bullseye == (0, 4):
            guessing = False
            print("Conratulations!")
        print()

def comGuess(number, filter=False, guessList=list(map(str,range(0,10)))):
    if len(guessList) == 4:
        answer = ['x'] * 4
        for digit in guessList:
            for i in range(4):
                guess = [filter] * 4
                guess[i] = digit
                if checkGuess(guess, number) == (0,1):
                    answer[i] = digit
                    print("Answer is: {}".format(answer))
                    break
        return ''.join(answer)

    else:
        guess = ''.join(guessList[:4])
        bullseye = checkGuess(guess, number)
        # All four numbers not in answer
        if bullseye == (0, 0):
            if not filter: filter = guess[0]
            for digit in guess:
                guessList.remove(digit)
                print("Narrowing numbers to: {}".format(guessList))
        else:
            totalCorrect = bullseye[0] + bullseye[1]
            correct = []
            for digit in guess:
                if checkGuess(digit*4, number) == (0, 0):
                    if not filter: filter = digit
                    guessList.remove(digit)
                    print("Narrowing numbers to: {}".format(guessList))
                else:
                    guessList.remove(digit)
                    guessList.append(digit)

    return comGuess(number, filter, guessList)


print("Welcome to Bullseye! Would you like to guess the number, or let the computer guess?")
print("1. Guess the number!")
print("2. Let the computer guess!")
print("3. Exit")


choice = input("Your choice: ")
print()
while choice not in list(map(str,range(1,4))):
    choice = input("That is not a valid option. Please choose a number from 1 to 3\n")
    print()
if choice == '1':
    userGuess()
elif choice == '2':
    number = getInput()
    while not number:
        number = getInput()
    if number != '####':
        print("\n{} is the guess of the computer!".format(comGuess(number)))

print("Thanks for playing!")
