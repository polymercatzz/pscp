"""[Midterm 2020] Pringles"""
def main():
    """[Midterm 2020] Pringles"""
    lid_1 = input()
    pringles = input()
    lid_2 = input()
    num = int(input())
    pring = 0
    found = 0
    for i in pringles:
        if i == ")":
            pring += 1
    for i in range(num):
        if pringles[i] == ")":
            found += 1
        if i == num-1:
            pringles = " "*num + pringles[num:]
    print(found)
    if found >= pring:
        print("None.")
    else:
        print("There are still some left.")
    print(lid_1)
    print(pringles)
    print(lid_2)
main()
