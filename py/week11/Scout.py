"""Scout"""
def main(test):
    """Scout"""
    result = []
    for _ in range(test):
        test_egg = input().split(" ")
        egg = sorted(input().split(" "), key=float)
        weight = 0
        count = 0
        for check in range(int(test_egg[0])):
            if weight+float(egg[check]) <= int(test_egg[2]):
                weight += float(egg[check])
                count += 1
        result.append(min(int(test_egg[1]), count))
    print(*result, sep="\n")
main(int(input()))
