"""Point Sorting"""
def sort_result(numx):
    """"sort list by numx+numy"""
    return int(numx[0])+int(numx[1]), -int(numx[1])
def main(num):
    """Point Sorting"""
    for _ in range(num):
        group = int(input())
        result = []
        for _ in range(group):
            word = tuple(input().split())
            result.append(word)
            result.sort(key=sort_result)
        for i in result:
            numx, numy = i[0], i[1]
            print(numx, numy)
main(int(input()))
