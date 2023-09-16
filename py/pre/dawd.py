def cal(lst):
    min_pair_sum = 0
    min_pair = []
    lst = sorted(lst, reverse=True)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            pair_sum = lst[i] - lst[j]
            if min_pair_sum == 0:
                min_pair_sum = pair_sum
            elif pair_sum < min_pair_sum:
                min_pair_sum = pair_sum
                min_pair = [lst[i], lst[j]]
    for i in min_pair:
        if i in lst:
            lst.remove(i)
    return lst
def main():
    num_1 = int(input())
    lst = [3, 4, 7, 9, 1, 1]
    for num in range(num_1):
        lst = cal(lst)
    print(lst)
main()
