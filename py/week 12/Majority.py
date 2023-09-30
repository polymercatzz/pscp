"""Majority"""
def main(candi, score):
    """Majority"""
    dict_candi = {}
    for order in range(1, candi+1):
        dict_candi[order] = 0
    for _ in range(score):
        whoo = int(input())
        dict_candi[whoo] += 1
    win = max(dict_candi, key=dict_candi.get)
    if max(dict_candi.values()) < score/2:
        win = 0
    print(win, max(dict_candi.values()))
main(int(input()), int(input()))
