import json
import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    
    # wrd = json.load(open("data.json"))
    # word = random.choice(wrd)
   # y = random.randrange(1,500)
   # x= wrd.keys[0]
   # wrd = random.choice(x)
   # print(wrd)
    # wrd = json.load(open("data.json"))
    # y = random.randrange(1,500)
    # x= wrd.keys[y]
    # word = random.choice(x)
    #print(word)
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("\nYou win!")
            break

        print("\nGuess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("\nEnter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("\n9 turns left")
                print("  --------  ")
            if turns == 8:
                print("\n8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("\n7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("\n6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("\n5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("\n4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("\n3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("\n2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("\n1 turns left")
                print("\nLast breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("\nYou loose")
                print("\nYou let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("\nEnter your name\n")
print("\n Welcome" , name )
print("-------------------")
print("\n Try to guess the word in less than 10 attempts \n")
hangman()
print()
