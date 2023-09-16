"Donut"
def main():
    "cal donut"
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    donut_box = num_d//(num_b+num_c)
    donut_result = donut_box*(num_b+num_c)
    num_d = num_d-donut_result
    if num_d >= num_b:
        num_d = 0
        donut_result = donut_result+num_b+num_c
        donut_box += 1
    else:
        donut_result = donut_result+num_d
    pri_donut = (donut_box*num_b)*num_a+num_d*num_a
    print(pri_donut, donut_result)
main()
