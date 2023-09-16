"""Difference"""
def main():
    """Difference"""
    num_n = int(input())
    num_k = int(input())
    seta = set()
    setb = set()
    for _ in range(num_n):
        seta.add(input())
    for _ in range(num_k):
        setb.add(input())
    if seta.intersection(setb) == set():
        print('Nope')
    else:
        print(*sorted(seta.intersection(setb), reverse=True), sep="\n")
main()
