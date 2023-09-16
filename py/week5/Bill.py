"""Bill"""
def main():
    """Bill"""
    price = int(input())
    ser = min(1000, max(price*0.1, 50))
    price = (price+ser)*1.07
    print("%.2f"%price)
main()
