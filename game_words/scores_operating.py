

def scores_count(try_left) -> int:
    scores = (1000 if try_left == 0 else 60)
    final_score = scores - try_left * 10
    return final_score


def score_records(file, scores):
    name = input("Enter your name:\n")
    score = scores
    with open(file, "a+") as file:
        file.write(f"{name} : {score}\n")


def score_represent():
    with open("score_records.txt", "r") as file:
        records = [users.strip() for users in file.readlines() if users != "\n"]
        print(records)
