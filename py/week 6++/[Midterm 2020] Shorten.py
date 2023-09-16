"""[Midterm 2020] Shorten"""
def main():
    """[Midterm 2020] Shorten"""
    num_f = 0
    num_m = 0
    result = ""
    while True:
        num = int(input())
        if num == -1:
            if num_f != num_m:
                result += "%d-%d"%(num_f, num_m)
            elif num_f == 0:
                result = ""
            else:
                result += "%d"%num_f
            break
        if num_f == 0:
            num_f = num
            num_m = num
        elif num-num_m == 1:
            num_m = num
        else:
            if num_f != num_m:
                result += "%d-%d, "%(num_f, num_m)
            else:
                result += "%d, "%num_f
            num_f = num
            num_m = num
    print(result)
main()
