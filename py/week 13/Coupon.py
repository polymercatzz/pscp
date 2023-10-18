"""Coupon"""
def main(price, pro):
    """Coupon"""
    pro[0] += [price]
    pro[1] += [price]
    if float(pro[0][2]) <= price:
        pro[0][3] = price-float(pro[0][1])
    if float(pro[1][2]) <= price:
        pro[1][3] = price*(100-float(pro[1][1]))/100
    result = sorted([i for i in pro if float(i[2]) <= price], \
            key=lambda x: (float(x[-1]), float(x[2])))
    print("%s %s"%((result[0][0]), round(result[0][-1], 1)) if result else "Nope")
main(float(input()), [[_]+input().split(" ") for _ in range(1, 3)])
