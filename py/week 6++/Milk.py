"""[Recommend] Milk"""
def main(price, faa, free, money):
    """[Recommend] Milk"""
    bottle = money//price
    result = bottle
    while bottle >= faa and faa != 0:
        pro_free = (bottle//faa)
        result += pro_free*free
        bottle = bottle-pro_free*faa+pro_free*free
    print(result)
main(int(input()), int(input()), int(input()), int(input()))
