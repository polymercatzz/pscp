"""Diamond I"""
def main():
    """Diamond I"""
    diamond = []
    floor = int(input())
    lenght = int(input())
    for _ in range(floor):
        dai = input().split()
        if diamond == []:
            for i in dai:
                diamond.append(int(i))
        else:
            for i in range(lenght):
                diamond[i] = int(dai[i])+int(diamond[i])
    print(max(diamond))
main()
