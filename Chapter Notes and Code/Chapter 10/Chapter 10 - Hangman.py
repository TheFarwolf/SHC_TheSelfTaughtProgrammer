#Applying current knowledge to make a game of hangman
def hangman(word):
    wrong  = 0
    stages = ["",
              "_________          ",
              "|        |         ",
              "|      ('')        ",
              "|     / || \       ",
              "|      /  \        ",
              "|                  ",
              "|                  ",]
    rLetters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while(wrong < len(stages) - 1):
        print("\n")
        msg = "Guess a letter: "
        char = raw_input(msg)
        if char in rLetters:
            cind = rLetters.index(char)
            board[cind] = char
            rLetters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

hangman("Cat")
