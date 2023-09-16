"""Difference"""
def main():
    """Difference"""
    num_n = int(input())
    num_k = int(input())
    seta = set()
    setb = set()
    for _ in range(num_n):
        seta.add(int(input()))
    for _ in range(num_k):
        setb.add(int(input()))
    print(*sorted(seta-setb))
main()
