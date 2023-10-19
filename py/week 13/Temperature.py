"""Temperature"""
def main(tem, word, word2):
    """Temperature"""
    if word == "F":
        tem = (tem-32)*5/9
    elif word == "K":
        tem = tem-273.15
    elif word == "R":
        tem = tem*5/9-273.15
    dict_word2 = {"C":tem, "F":tem*9/5+32, "K":tem+273.15, "R":(tem+273.15)*9/5}
    print("%.2f"%(dict_word2.get(word2)))
main(float(input()), input(), input())
