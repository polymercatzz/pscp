"""[Midterm 2020] One For All"""
def main():
    """[Midterm 2020] One For All"""
    num = int(input())
    word = ""
    for _ in range(1, num+1):
        word += input()
        if _ == num:
            word += "_%d"%num
        elif _%2 == 0:
            word += "-"*_
        else:
            word += "*"*_
    print(word)
main()
