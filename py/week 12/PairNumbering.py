"""PairNumbering"""
import json
def main(a_list, b_list, nump):
    """PairNumbering"""
    a_list = json.loads(a_list)
    b_list = json.loads(b_list)
    result = 0
    dict_b = {}
    dict_a = {}
    for i in b_list:
        dict_b[i] = dict_b.get(i, 0)+1
    for i in a_list:
        dict_a[i] = dict_a.get(i, 0)+1
    for i in dict_a:
        result += dict_b.get(nump-i, 0) * dict_a.get(i)
    print(result)
main(input(), input(), int(input()))
