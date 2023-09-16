"""[Recommend] Milk"""
def main():
    """[Recommend] Milk"""
    price = int(input())
    faa = int(input())
    free = int(input())
    money = int(input())
    bottle = money//price
    result = bottle
    if bottle >= faa and faa != 0:
        while bottle >= faa:
            pro_free = (bottle//faa)
            result += pro_free*free
            bottle = bottle-pro_free*faa+pro_free*free
    print(result)
main()
