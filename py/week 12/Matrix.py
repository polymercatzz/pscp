"""Matrix_MN"""
def main(numm, numn):
    """Matrix_MN"""
    num = []
    for _ in range(numm*numn):
        num.append(int(input()))
    for i in range(1, numm*numn+1):
        print(num[i-1], end=" ")
        if i%numn == 0:
            print()
main(int(input()), int(input()))
