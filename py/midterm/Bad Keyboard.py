"""Bad Keyboard"""
def main(word):
    """Bad Keyboard"""
    new = ""
    for i in word:
        if i == "o":
            new += "i"
        elif i == "i":
            new += "o"
        elif i == "O":
            new += "I"
        elif i == "I":
            new += "O"
        else:
            new += i
    print(new)

main(input())
