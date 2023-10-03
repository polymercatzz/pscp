"""Compound Interest"""
def main(money, interest, year):
    """Compound Interest"""
    for _ in range(year):
        money = money+(money*interest/100)
    print("%.2f"%money)
main(int(input()), float(input()), int(input()))
