"""MultiplyMatrixPQR"""
def main(nump, numq, numr):
    """MultiplyMatrixPQR"""
    matrix1 = [[int(input()) for j in range(numq)] for i in range(nump)]
    matrix2 = [[int(input()) for j in range(numr)] for i in range(numq)]
    ans = []
    for i in matrix1:
        for j in range(numr):
            result = 0
            for k in range(numq):
                result += i[k]*matrix2[k][j]
            ans.append(result)
    for i in range(1, nump*numr+1):
        print(ans[i-1], end=" ")
        if i%numr == 0:
            print()
main(int(input()), int(input()), int(input()))
