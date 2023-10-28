"""ClockHands"""
def main(hours, minute):
    """ClockHands"""
    hours = (5*hours+minute/12)%60
    if hours >= minute and hours%60 < minute+1:
        print("True")
    else:
        print("False")
main(int(input()), int(input()))
