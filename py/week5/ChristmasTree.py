"""christmas tree"""
def tree():
    """christmas tree"""
    num_n = int(input())
    num_k = int(input())
    space = num_n - 1
    star = 1
    for _ in range(num_n):
        print(" "*space, end="")
        print("*"*star, end="")
        star += 2
        space -= 1
        print()
    print((" "*(num_n-2)+"---\n")*num_k)
tree()
