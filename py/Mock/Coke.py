"""Coke"""
def main():
    """Coke"""
    price = int(input())
    pro = int(input())
    price_dis = int(input())
    want = int(input())
    if pro > 0:
        pro_set = want//pro
        if want%pro == 0:
            pro_set -= 1
        if want > 0:
            money = pro_set*price_dis+(want-pro_set)*price
        else:
            money = 0
    else:
        money = want*price
    print(money)
main()
