"""Factors"""
def main(num):
    """Factors"""
    for _ in range(num):
        number = int(input())
        result = []
        while number != 1:
            for i in range(2, number+1):
                if  number%i == 0:
                    number //= i
                    result.append(i)
                    break
        for j, i in enumerate(sorted(set(result))):
            if result.count(i) > 1:
                print("%d**%d"%(i, result.count(i)), end=" ")
            else:
                print(i, end=" ")
            if j != len(set(result))-1:
                print("x", end=" ")
        print()
main(int(input()))
