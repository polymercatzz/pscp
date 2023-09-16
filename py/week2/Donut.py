"Donut"
def main():
    "Donut"
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    donut_pi = 0
    donut_re = 0
    if num_c > 0 and num_d > 0 and num_d > num_b:
        donut_1 = num_d//(num_b+num_c)
        if donut_1 > 0:
            num_d = num_d-donut_1*(num_b+num_c)
            donut_re = donut_1*(num_b+num_c)
            donut_pi = donut_1*num_b
            if num_d >= num_b:
                num_d = num_d-num_b
                donut_re = donut_re+num_b+num_c
                donut_pi = donut_pi+num_b
            else:
                donut_re = donut_re+num_d
                donut_pi = donut_pi+num_d
        else:
            num_d = num_d-num_b
            donut_re = donut_re+num_b+num_c
            donut_pi = donut_pi+num_b
    elif num_c > 0 and num_d > 0 and num_d == num_b:
        if num_d > num_c:
            donut_pi = num_d-num_c
            donut_re = num_d
        else:
            donut_pi = num_d
            donut_re = num_d+num_c
    else:
        donut_pi = num_d
        donut_re = num_d
    result = donut_pi*num_a
    print(result, donut_re)
main()
