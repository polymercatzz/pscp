"""SMS"""
def sms(times):
    """SMS"""
    dict_sms = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
    result = ""
    for _ in range(times):
        num = int(input())
        pess = int(input())
        if num == 1:
            result = result[:-pess]
        else:
            result += dict_sms.get(num)[pess%len(dict_sms.get(num))-1]
    print("null" if result == "" else result)
sms(int(input()))
