

def word_validation(input_word) -> bool:
    if len(input_word) != 5 or not input_word.isascii():
        print("Invalid enter!")
        return True
    else:
        return False
