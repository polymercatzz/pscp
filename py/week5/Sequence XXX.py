"""Sequence 30"""
def main():
    """Sequence 30"""
    num_n = int(input())
    num_m = int(input())
    for i in range(num_n):
        word = ""
        for j in range(num_n):
            if j == 0 or j == num_n-1 or i == j or i+j == num_n-1 or i == 0 or i == num_n-1:
                word += "*"
            else:
                word += " "
        print((word+" ")*num_m)
main()
