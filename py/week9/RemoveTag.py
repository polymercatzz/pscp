"""RemoveTag"""
def main():
    """RemoveTag"""
    word = input()
    word2 = []
    word3 = []
    if ">" in word:
        word = word.split(">")
        for i in word:
            if i == "":
                pass
            elif i[0] != "<" and "<" in i:
                word2.append(i[0:i.find("<")].strip())
            elif "<" not in i:
                word2.append(i)
        for i in word2:
            if " " in i:
                word3.extend(i.split())
            elif i != "":
                word3.append(i)
        print(word3)
    else:
        word = word.split()
        print(word)
main()
