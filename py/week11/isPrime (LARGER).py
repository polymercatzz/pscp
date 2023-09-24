"""isPrime (LARGER)"""
def prime():
    """isPrime (LARGER)"""
    num = int(input())
    result = "False"
    if num <= 1:
        result = "False"
    elif num <= 3:
        result = "True"
    elif num % 2 == 0 or num % 3 == 0:
        result = "False"
    else:
        test = 5
        while test * test <= num:
            if num % test == 0 or num % (test+2) == 0:
                result = "False"
                break
            test += 6
            result = "True"
    print(result)
prime()
