"""CoinChangev1"""
def main(money):
    """CoinChangev1"""
    lst_coin = [25, 10, 5, 1]
    coin = 0
    for i in lst_coin:
        coin += money//i
        money -= (money//i)*i
    print(coin)
main(int(input()))
