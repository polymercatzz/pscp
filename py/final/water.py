"""Water"""
def main(month):
    """Water"""
    result = 0
    price = float(input())
    high = float(input())
    h_price = float(input())
    low = float(input())
    for _ in range(month):
        use = float(input())
        use_month = 0
        if use > high:
            use_month += (use-high)*h_price
            use = high
        use_month += use*price
        if use_month <= low:
            use_month = 0
        result += use_month
    print("%.2f"%(result))
main(int(input()))
