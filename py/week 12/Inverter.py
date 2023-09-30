"""Inverter"""
def main(num_2):
    """Inverter"""
    dict_num = {"1":"0", "0":"1"}
    result = ""
    for i in num_2:
        result += dict_num.get(i)
    if int(result) == 0:
        print()
    else:
        print(int(result))
main(input())
