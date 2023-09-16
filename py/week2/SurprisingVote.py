"SurprisingVote"
def main():
    "SurprisingVote"
    sum_score = float(input())
    high_score = float(input())
    score = sum_score-high_score
    if score-high_score < 0:
        score = 0
    else:
        score = score-high_score
    if high_score-score <= 2:
        print("Not surprising")
    else:
        print("Surprising")

main()
