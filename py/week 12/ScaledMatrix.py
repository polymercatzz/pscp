"""ScaledMatrix"""
def main(row, col):
    """ScaledMatrix"""
    matrix = [float(input()) for _ in range(row*col)]
    high = max(matrix)
    low = min(matrix)
    for i in range(1, row*col+1):
        print("%.2f"%((matrix[i-1]-low)/(high-low)), end=" ")
        if i%col == 0:
            print()
main(int(input()), int(input()))
