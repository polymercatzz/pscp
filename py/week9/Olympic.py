"""Olympic"""
def main(num):
    """Olympic"""
    order = 1
    rank = []
    for _ in range(num):
        rank.append(tuple(input().split(" ")))
    rank.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3]), x[0]))
    for i in range(1, len(rank)+1):
        if rank[i-1][1:] == rank[i-2][1:]:
            print(order, end=" ")
        else:
            order = i
            print(i, end=" ")
        print(*rank[i-1], end=" ")
        print(int(rank[i-1][1])+int(rank[i-1][2])+int(rank[i-1][3]))
main(int(input()))
