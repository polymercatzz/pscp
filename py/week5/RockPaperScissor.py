"""RockPaperScissor"""
def flight(word):
    """RockPaperScissor"""
    score_a = 0
    score_b = 0
    for i in range(0, len(word), 2):
        soo = word[i:i+2]
        if soo == "RP":
            score_b += 1
        elif soo == "PR":
            score_a += 1
        elif soo == "PS":
            score_b += 1
        elif soo == "SP":
            score_a += 1
        elif soo == "SR":
            score_b += 1
        elif soo == "RS":
            score_a += 1
    if score_a > score_b:
        print("A win %d-%d"%(score_a, score_b))
    elif score_a < score_b:
        print("B win %d-%d"%(score_b, score_a))
    else:
        print("DRAW %d"%score_a)
flight(input())
