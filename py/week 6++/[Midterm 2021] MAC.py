"""[Midterm 2021] MAC"""
def main(code):
    """[Midterm 2021] MAC"""
    num_base16 = '0123456789abcdefgABCDEFG'
    check = 0
    for i in code:
        if i in num_base16:
            check += 1
    if check == 12 and code[2::3] == "-----" and code.count("-") == 5:
        print("VALID 1")
    elif check == 12 and code[2::3] == ":::::" and code.count(":") == 5:
        print("VALID 2")
    elif check == 12 and code[4::5] == ".." and code.count(".") == 2:
        print("VALID 3")
    else:
        print("ERROR")
main(input())
