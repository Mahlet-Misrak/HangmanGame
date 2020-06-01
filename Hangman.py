import random
def hangman():
     word = ["rat","apple","ball","cat","bird","fish","snake","swan","dolphin","tiger"]
     theword = random.choice(word)
     print("Hint: The word has %s digits" %len(theword))

     turn = 10
     guessmade = ''

     while len(theword) > 0:
        main = ""
        for letter in theword:
            if letter in guessmade:
               main = main + letter
            else:
               main = main + "_" + ""
        if main == theword:
             print(main)
             print(" you won")
             break

        print("Guess the a letter from the word: ", main)
        guess = raw_input()

        if guess.isalpha():
            guessmade = guessmade + guess
        else:
           print("Please enter characters A-Z only")
        if guess in main:
            print("You have guessed the letter before")
        if guess not in theword:
            turn = turn - 1
            if turn == 9:
                print(" 9 turns left")
                print("------------")
            if turn == 8:
                print(" 8 turns left")
                print("------------")
                print("     0      ")
            if turn == 7:
                print("7 turns left")
                print("------------")
                print("     0      ")
                print("     |      ")
            if turn == 6:
                print("6 turns left")
                print("------------")
                print("     0      ")
                print("     |      ")
                print("    /       ")
            if turn == 5:
                print("5 turns left")
                print("------------")
                print("     0      ")
                print("     |      ")
                print("    / \     ")
            if turn == 4:
                print("4 turns left")
                print("------------")
                print("   \ 0      ")
                print("     |      ")
                print("    / \     ")
            if turn == 3:
                print("3 turns left")
                print("------------")
                print("   \ 0 /    ")
                print("     |      ")
                print("    / \     ")
            if turn == 2:
                print("2 turns left")
                print("------------")
                print("   \ 0 /|   ")
                print("     |      ")
                print("    / \     ")
            if turn == 1:

                print('1 turn left last chance %s' %x)
                print("------------")
                print("   \ 0_|    ")
                print("     |      ")
                print("    / \     ")
            if turn == 1:
                print("Game Over!!The man is dead")
                print("------------")
                print("     0_|    ")
                print("    /|\     ")
                print("    / \     ")
                break

x = raw_input("Enter your name : ")
print('Welcome to the game %s' %x)
print('----------------------------')
print('Try to guess the word in less than 10 attempts')
hangman()
