import sys
list1 = sys.argv[1]
list2 = sys.argv[2]
list3 = []
list2 = list2.split(",")
list1 = list(list1)
sayac = 5
inmode = True
outmode = False
usedin = []
usedout = []
repeat = 0
print("You have {} guesses left.".format(sayac))
for i in range(0,len(list1)):
    list3.append("-")
print(list3)
print("-----------------------------------")
for letter in list2:
    if inmode == True and letter in list1 and letter not in usedin:
        usedin.append(letter)
        if sayac <= 0:
            print("You lost the game")
            repeat = 1
            break
        for sira,harf in enumerate(list1):
            if harf == letter:
                list3[sira] = letter
        print("Guessed word : {} You are in IN mode".format(letter))
        print("You have {} guesses left.".format(sayac))
        print(list3)
        print("-----------------------------------")
        if list3 == list1:
            print("You won the game")
            break
    elif (letter not in list1 or letter in usedin) and inmode == True:
        inmode = False
        outmode = True
        sayac-=1
        if sayac < 0:
            print("You lost the game")
            repeat = 1
            break
        if letter in usedin:
            print("Guessed word : {} is used in IN mode. The game turned into OUT mode ".format(letter))
            print("You have {} guesses left.".format(sayac))
            print(list3)
            print("-----------------------------------")
        else:
            print("Guessed word : {} The game turned into OUT mode ".format(letter))
            print("You have {} guesses left.".format(sayac))
            print(list3)
            print("-----------------------------------")
        usedin.append(letter)
    elif outmode == True and letter not in list1 and letter not in usedout:
        usedout.append(letter)
        inmode = True
        outmode = False
        if sayac <= 0:
            print("You lost the game")
            repeat = 1
            break
        print("Guessed word : {} The game turned into IN mode ".format(letter))
        print("You have {} guesses left.".format(sayac))
        print(list3)
        print("-----------------------------------")
    elif (letter in list1 or letter in usedout) and outmode == True:
        inmode = False
        outmode = True
        sayac-=1
        if sayac < 0:
            print("You lost the game")
            repeat = 1
            break
        if letter in usedout:
            print("Guessed word : {} is used in OUT mod. You are in OUT mode".format(letter))
            print("You have {} guesses left.".format(sayac))
            print(list3)
            print("-----------------------------------")
        else:
            print("Guessed word : {} You are in OUT mode".format(letter))
            print("You have {} guesses left.".format(sayac))
            print(list3)
            print("-----------------------------------")
        usedout.append(letter)
if list1 != list3 and repeat != 1:
    print("You finished all letters")
    print("You lost the game")
