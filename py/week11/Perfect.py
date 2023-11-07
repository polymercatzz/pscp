"""Perfect"""
def main(num):
    """Perfect"""
    perfect = []
    for i in range(6, num+1, 2):
        cal = [1]
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                cal.extend([j, i//j])
        if sum(cal) == i:
            perfect.append(sum(cal))
    print(sum(perfect))
main(int(input()))
