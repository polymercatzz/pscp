"WeightStation"
def main():
    "WeightStation"
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())
    weight_4 = float(input())
    weight_err = weight_1*4-weight_2-weight_3-weight_4
    if weight_err+weight_2+weight_3+weight_4 >= 15000:
        print("Overweight")
    elif weight_1/2 <= weight_2 <= weight_1+weight_1/2 and \
        weight_1/2 <= weight_3 <= weight_1+weight_1/2 and \
            weight_1/2 <= weight_4 <= weight_1+weight_1/2 and \
                weight_1/2 <= weight_err <= weight_1+weight_1/2:
        print("Pass %.2f"%weight_err)
    else:
        print("Unbalance")
main()
