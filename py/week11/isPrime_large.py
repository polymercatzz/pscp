"""isPrime_large"""
def prime():
    """isPrime_large"""
    num = int(input())
    result = "NO"
    if num <= 1:
        result = "NO"
    elif num <= 3:
        result = "YES"
    elif num % 2 == 0 or num % 3 == 0:
        result = "NO"
    else:
        test = 5
        while test * test <= num:
            if num % test == 0 or num % (test+2) == 0:
                result = "NO"
                break
            test += 6
            result = "YES"
    print(result)
prime()
