"""Volleyball"""
def main():
    """Volleyball"""
    word = input()
    score_a = 0
    score_b = 0
    score_set_a = 0
    score_set_b = 0
    set_ = 1
    long_word = len(word)
    time_ = 0
    for i in word+" ":
        if i == "A":
            score_a += 1
        elif i == "B":
            score_b += 1
        if ((score_a >= 25 or score_b >= 25) or ((score_a >= 15 or score_b >= 15) and set_ >= 5)) \
            and abs(score_b-score_a) >= 2:
            print("Set %d: A (%d) | B (%d)"%(set_, score_a, score_b))
            if score_a > score_b:
                score_set_a += 1
            else:
                score_set_b += 1
            score_a = 0
            score_b = 0
            set_ += 1
        if long_word == time_ and not (score_set_a >= 3 or score_set_b >= 3):
            print("Set %d: A (%d) | B (%d)"%(set_, score_a, score_b))
        time_ += 1
    if abs(score_set_a-score_set_b) < 3 and set_ < 5 or score_set_a == score_set_b:
        print("The game has not finished yet.")
    elif score_set_a > score_set_b:
        print("A won %d:%d set"%(score_set_a, score_set_b))
    else:
        print("B won %d:%d set"%(score_set_b, score_set_a))
main()
