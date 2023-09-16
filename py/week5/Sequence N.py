"""Sequence N"""
def build_n(num):
    """Sequence N"""
    for i in range(num):
        for j in range(num):
            if j == 0 or j == num-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
build_n(int(input()))
