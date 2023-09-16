"""RuleofThree"""
def main():
    """RuleofThree"""
    num = int(input())
    high = 0
    for _ in range(num):
        price = float(input())
        weight = float(input())
        if weight/price > high or high == 0:
            price_bes = price
            weight_bes = weight
            high = weight/price
        elif weight/price == high:
            if price_bes > price:
                price_bes = price
                weight_bes = weight
                high = weight/price
    print("%.2f %.2f"%(price_bes, weight_bes))
main()
