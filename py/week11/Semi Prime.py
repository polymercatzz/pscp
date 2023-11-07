"""Semi Prime"""
def main(num):
    """Semi Prime"""
    ans = []
    for i in range(2, num+1):
        factor = []
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                factor.extend([j, i//j])
        if len(factor) == 2 and (factor[1] == factor[0] or factor[1]%factor[0] != 0):
            ans.append(1)
    print(sum(ans))
main(int(input()))
