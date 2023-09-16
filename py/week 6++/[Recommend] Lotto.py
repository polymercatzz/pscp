"""[Recommend] Lotto"""
def lotto():
    """[Recommend] Lotto"""
    prize_1 = input()
    prize_e_2 = input()
    prize_f_31 = input()
    prize_f_32 = input()
    prize_e_31 = input()
    prize_e_32 = input()
    lottery = input()
    if prize_1 == "000000":
        prize_1_low = "999999"
        prize_1_high = "000001"
    elif prize_1 == "999999":
        prize_1_low = "999998"
        prize_1_high = "000000"
    else:
        prize_1_low = "%06d"%(int(prize_1)-1)
        prize_1_high = "%06d"%(int(prize_1)+1)
    win = 0
    if prize_1 == lottery:

        win += 6000000
    elif lottery == prize_1_high or lottery == prize_1_low:
        win += 100000
    if prize_e_2 == lottery[-2:]:
        win += 2000
    if prize_f_31 == lottery[:3]:
        win += 4000
    if prize_f_32 == lottery[:3]:
        win += 4000
    if prize_e_31 == lottery[-3:]:
        win += 4000
    if prize_e_32 == lottery[-3:]:
        win += 4000
    print(win)

lotto()
