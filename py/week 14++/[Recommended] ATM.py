"""[Recommended] ATM"""
def main(money):
    """[Recommended] ATM"""
    while True:
        order = input().split(" ")
        if order == ["END"]:
            print(money)
            break
        d_money = {"W":-min(money, int(order[1]))}
        money += d_money.get(order[0], int(order[1]))
main(int(input()))
