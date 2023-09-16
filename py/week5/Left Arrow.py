"""Left Arrow"""
def arrow_l(num_k, num_n):
    """Left Arrow"""
    for i in range(num_n):
        print(" "*abs(num_n//2-i)+"*"*num_k)
arrow_l(int(input()), int(input()))
