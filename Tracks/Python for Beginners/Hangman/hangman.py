import random
game = input('Type "play" to play the game, "exit" to quit: ')
if game == "play":
    lst = ["python", "java", "kotlin", "javascript"]
    used_letters = []
    word = random.choice(lst)
    print("H A N G M A N")
    word_ = len(word)
    word2 = word_ * ['-']
    count = 8
    while count > 0:
        print()
        print("".join(word2))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        used_letters.append(letter)
        if used_letters.count(letter) != 1:
            print("You've already guessed this letter")
            continue
        if letter in word:
            for i in range(word_):
                if word[i] == letter:
                    word2[i] = letter
        elif not letter.islower() or not letter.isalpha():
            print("Please enter a lowercase English letter")
        else:
            count -= 1
            print("That letter doesn't appear in the word")
        if "".join(word2) == word:
            print(f'You guessed the word {"".join(word2)}!')
            print("You survived!")
            break
    else:
        if count == 0:
            print("You lost!")
