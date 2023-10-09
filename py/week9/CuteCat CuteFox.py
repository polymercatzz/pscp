"""CuteCat CuteFox"""
def main(num):
    """CuteCat CuteFox"""
    cat_check = True
    fox_check = True
    cat = 0
    fox = 0
    animal = {}
    result = {}
    for _ in range(num):
        word = input()
        animal.update({word[2:(word.find(":"))-2]:word[(word.find(":"))+3:-2]})
    for key, value in animal.items():
        if value == "Fox01" or key == "Fubuki":
            fox_check = False
        if value == "Cat01" or key == "Garfield":
            cat_check = False
        result[value] = key
    if cat_check:
        result.setdefault("Cat01", "Garfield")
    if fox_check:
        result.setdefault("Fox01", "Fubuki")
    result = dict(sorted(list(result.items()), key=lambda x: (ord(x[0][0]), int(x[0][3:]))))
    for i in result.keys():
        if "Fox" in i:
            fox += 1
        elif "Cat" in i:
            cat += 1
    print("Cat : %d"%cat)
    print("Fox : %d"%fox)
    for value, key in result.items():
        print(key, value, sep=" : ")
main(int(input()))
