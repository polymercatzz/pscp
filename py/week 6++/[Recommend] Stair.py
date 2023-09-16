"""[Recommend] Stair"""
def main():
    """[Recommend] Stair"""
    high = int(input())
    stair = int(input())
    up_ = 0
    dubble = 0
    for _ in range(stair):
        h_stair = int(input())
        if h_stair <= high and up_ != "NO":
            if h_stair == high or dubble + h_stair == high\
                or dubble + h_stair < high and _ == stair-1:
                up_ += 1
                dubble = 0
            elif dubble + h_stair > high and _ == stair-1:
                up_ += 2
            elif dubble + h_stair > high:
                dubble = h_stair
                up_ += 1
            else:
                dubble += h_stair
        else:
            up_ = "NO"
    print(up_)

main()
