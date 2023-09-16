"""Inflation"""
def main():
    """Inflation"""
    num_n = int(float(input())*100)
    num_k = int(input())
    for _ in range(num_k):
        num_n = num_n + num_n*381//10000
    print("%d.%02d"%(num_n//100, num_n%100))
main()
