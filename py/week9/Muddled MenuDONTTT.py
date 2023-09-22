"""Muddled Menu"""
def main():
    """Muddled Menu"""
    menu = []
    dont = []
    result = []
    while True:
        word = input()
        if word == "DONE":
            break
        elif word == "SOMETHING'S WRONG":
            menu.clear()
        elif word == "CLOSED":
            menu.clear()
            break
        elif "Can't do:" in word:
            dont += word.split("Can't do: ")
        elif "#N" not in word:
            menu.insert(int(word[word.find("#")+1])-1, word)
        else:
            menu.append(word)
    for i in menu:
        if i[:i.find("#")-1] not in dont:
            result.append(i[:i.find("#")-1])
    print("Full Course:", result, end=" ")
    result.reverse()
    print("Reversed:", result, end="")
main()
