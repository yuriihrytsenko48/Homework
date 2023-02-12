import random
import scores_operating as so
import words_file_operating as wfo
import words_game_logic as wgl

try_count = 0
word_file = "word_file.txt"
scores_file = "score_records.txt"

words = wfo.words_loading(word_file)
answer_word = random.choice(words)
print(answer_word)
print("Enter record to see records or word to start a game")

while try_count <= 6:

    word = input("Enter word with 5 letters in latin.\n").lower().strip()

    if word == "quit":
        break

    if word == "record":
        so.score_represent()
        continue
    elif wfo.word_validation(word):
        continue

    if word == answer_word:
        print(answer_word.title())
        print(f"Your scores is {so.scores_count(try_count)}")

        ask = input("Do you want to save "
                    "your record? Y/N\n").lower().strip()
        if ask == "y":
            so.score_records(scores_file, so.scores_count(try_count))

        if input("As a winner "
                 "you can add a new word! "
                 "Will you? Y/N\n").strip().lower() == "y":
            while True:
                new_word = input("Enter new word:\n").strip().lower()
                if wfo.word_validation(new_word):
                    continue
                elif new_word in words:
                    print("The word is already exists! Try again!")
                    continue
                else:
                    words.append(new_word.strip().title() + "\n")
                    wfo.words_saving(word_file, words)
                    break
            break

    else:
        guess = wgl.guess_logic(word, answer_word)
        print(guess)
        try_count += 1
else:
    try_count = 0
    print(answer_word.title())
