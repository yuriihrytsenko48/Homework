

def guess_logic(guess_word, answer_word):

    guess_word = list(guess_word)
    answer_word = list(answer_word)
    guess = []

    for letter1, letter2 in zip(guess_word, answer_word):
        if letter1 == letter2:
            guess.append(letter1)
            answer_word.insert(answer_word.index(letter2) + 1, "_")
            answer_word.pop(answer_word.index(letter2))
        else:
            guess.append("_")

    guess = "".join(guess)

    for letter in guess_word:
        if answer_word.count("_") == 5:
            break
        else:
            if letter in answer_word:
                guess = guess.replace("_", "?", 1)

    guess = guess.replace("_", ".")
    return guess
