"""T-score"""
def main(people, _):
    """T-score"""
    score = [int(input()) for _ in range(people)]
    sd_score = (sum(list(map(lambda x: (x-(sum(score)/people))**2, score)))/(people-1))**0.5
    for i in score:
        print("%.2f"%(50+10*((i-sum(score)/people)/sd_score)))
main(int(input()), int(input()))
