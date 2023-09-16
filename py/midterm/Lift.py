"""Lift"""
def main(people, weight):
    """Lift"""
    all_weight = 0
    adult = False
    for _ in range(people):
        if int(input()) >= 12:
            adult = True
        all_weight += float(input())
    if adult and all_weight <= weight or people == 0:
        print("Safe")
    else:
        print("Not Safe")

main(int(input()), float(input()))
