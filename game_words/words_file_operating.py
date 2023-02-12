from words_validation import word_validation


def words_loading(file):
    with open(file, "r") as source_file:
        lines = [word.strip().lower() for word in source_file if word != "\n"]
        return lines


def words_saving(file, words):
    with open(file, "w") as source_file:
        for word in words:
            title_word = word.title()
            source_file.write(title_word + "\n")
