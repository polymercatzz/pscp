"""SecondConverter"""
def main():
    """SecondConverter"""
    num_k = int(input())
    num_s = int(input())
    num_m = int(input())
    num_h = int(input())
    minute = num_k//num_s
    second = num_k%num_s
    hours = minute//num_m
    minute = minute%num_m
    hours = hours%num_h
    print("%d:%d:%d"%(hours, minute, second))
main()
