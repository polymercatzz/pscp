"""Stamps"""
import math
def main(time, pro, stamp_b, stamp_c, discount):
    """Stampss"""
    stamp = 0
    result = 0
    for _ in range(time):
        price = int(input())
        if stamp >= stamp_c:
            dis = min(price, discount*(stamp//stamp_c))
            price -= dis
            stamp -= math.ceil(dis/discount)*stamp_c
        if price >= pro:
            stamp += stamp_b*(price//pro)
        result += price
    print(result, stamp, sep="\n")
main(int(input()), int(input()), int(input()), int(input()), int(input()))
