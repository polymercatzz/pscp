"""Grade III"""
def main():
    """Grade III"""
    sub = int(input())
    score = 0
    for _ in range(sub):
        score_2 = float(input())
        if score_2 >= 95 and score_2 <= 100:
            score += 4
        elif score_2 >= 90 and score_2 < 95:
            score += 3.5
        elif score_2 >= 85 and score_2 < 90:
            score += 3
        elif score_2 >= 80 and score_2 < 85:
            score += 2.5
        elif score_2 >= 75 and score_2 < 80:
            score += 2
        elif score_2 >= 70 and score_2 < 75:
            score += 1.5
        elif score_2 >= 65 and score_2 < 70:
            score += 1
        elif score_2 >= 60 and score_2 < 65:
            score += 0.5
        elif score_2 >= 0 and score_2 < 60:
            score += 0
    result = score/sub-0.005
    print("%.2f"%result)
main()
