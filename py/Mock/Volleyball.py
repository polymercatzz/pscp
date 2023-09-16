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
    for i in word:
        
        if i == "A":
            score_a += 1
        elif i == "B":
            score_b += 1
        time_ += 1
        if abs(score_a-score_b) >= 2 and (score_a >= 14 or score_b >= 14) \
            or long_word == time_ and set_ == 5:
            print("Set %d: A (%d) | B (%d)"%(set_, score_a, score_b))
            if score_a > score_b:
                score_set_a += 1
            else:
                score_set_b += 1
            score_a = 0
            score_b = 0
            set_ += 1
        if abs(score_a-score_b) >= 2 and (score_a >= 25 or score_b >= 25) \
            or long_word == time_:
            print("Set %d: A (%d) | B (%d)"%(set_, score_a, score_b))
            if score_a > score_b:
                score_set_a += 1
            else:
                score_set_b += 1
            score_a = 0
            score_b = 0
            set_ += 1
    if score_set_b > score_set_a and score_set_b >= 3:
        print("B won %d:%d set"%(score_set_b, score_set_a))
    elif score_set_a > score_set_b and score_set_b >= 3:
        print("A won %d:%d set"%(score_set_a, score_set_b))
    elif score_a == 0 and score_b == 0:
        print("Set %d: A (0) | B (0)"%set_)
    else:
        print("The game has not finished yet.")
main()
