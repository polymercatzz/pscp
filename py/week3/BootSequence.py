"""BootSequence"""
def main():
    """BootSequence"""
    num = int(input())
    for _ in range(1, num+1):
        if _ < num:
            print(_, end="_")
        else:
            print(_)

main()
