"Stepper II"
def main():
    "Stepper II"
    num_m = int(input())
    num_n = int(input())
    for _ in range(abs(num_m-num_n)+1):
        print(num_m)
        if num_m < num_n:
            num_m += 1
        else:
            num_m -= 1

main()
