"Left Arrow"
def main():
    "main"
    num_k = int(input())
    num_n = int(input())
    times_ = True
    space_ = num_n//2
    for num_n in range(num_n):
        if space_ > 0 and times_:
            print(" "*space_+"*"*num_k)
            space_ -= 1
        elif space_ == 0:
            print("*"*num_k)
            times_ = False
            space_ += 1
        else:
            print(" "*space_+"*"*num_k)
            space_ += 1
main()
