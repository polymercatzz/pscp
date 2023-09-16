"""Sequence XI"""
def main():
    """Sequence XI"""
    num_1 = int(input())
    for i in range(-num_1+1, num_1):
        for j in range(-num_1+1, num_1):
            print("%02d"%(num_1-max(abs(i), abs(j))), end=" ")
        print()
main()
