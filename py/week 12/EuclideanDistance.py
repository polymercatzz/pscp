"""EuclideanDistance"""
def main(num):
    """EuclideanDistance"""
    result = 0
    dot = [list(map(int, input().split())) for i in range(num)]
    for i, data in enumerate(dot[1:]):
        result += ((dot[i][0]-data[0])**2+(dot[i][1]-data[1])**2)**0.5
    print("%.2f"%result)
main(int(input()))
