"""Inflation"""
def main():
    """Inflation"""
    num_n = float(input())
    num_k = int(input())
    for _ in range(num_k):
        if num_n <= 0:
            break
        num_n = round(num_n*1.0381-0.005, 2)
    print("%.2f"%num_n)
main()
