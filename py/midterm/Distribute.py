"""Distribute"""
def main(money, people):
    """Distribute"""
    money = money-people
    eight_can = money//7
    can_give = min(eight_can, max(people-1, 0))
    people = people-can_give
    money -= (can_give*7)
    if people == 1 and money == 3:
        can_give -= 1
    elif money == 7:
        can_give += 1
    print(max(-1, can_give))
main(int(input()), int(input()))
