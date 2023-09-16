"""home run"""
def main():
    """home run"""
    num = int(input())
    dis = float(input())
    home = 0
    for _ in range(num):
        if float(input()) < dis:
            home += 1
    print(home)

main()
