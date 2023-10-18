"""Muddled Menu"""
def main():
    """Muddled Menu"""
    menu = []
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
            print(word.replace("Can't do: ", ""))
            menu.remove(word.replace("Can't do: ", ""))
        elif "#N" not in word:
            menu.insert(int(word[word.find("#")+1:])-1, word[:word.find("#")-1])
        else:
            menu.append(word[:word.find("#")-1])
    print("Full Course:", menu, "Reversed:", list(reversed(menu)))
main()
