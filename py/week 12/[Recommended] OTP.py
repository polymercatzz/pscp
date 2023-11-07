"""[Recommended] OTP"""
def main():
    """[Recommended] OTP"""
    while True:
        otp = input()
        if otp == "0":
            break
        dict_otp = {}
        for i in otp:
            dict_otp[i] = dict_otp.get(i, 0) + 1
        dict_max = [list(dict_otp.values()).count(2), list(dict_otp.values()).count(3)]
        if len(otp) == 4 and dict_max == [1, 0]:
            print("Valid")
        elif len(otp) == 6 and dict_max in [[2, 0], [1, 1], [0, 1]]:
            print("Valid")
        elif len(otp) == 8 and dict_max in [[3, 0], [1, 2], [0, 2]]:
            print("Valid")
        else:
            print("Invalid")
main()
 