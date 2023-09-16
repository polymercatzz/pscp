"""Future Message"""
def main():
    """Future Message"""
    word = input()
    if word.isnumeric():
        print("Number")
    elif word.isupper():
        print("Uppercase")
    elif word.islower():
        print("Lowercase")
    elif word.istitle():
        print("Title")
    elif word.isspace():
        print("Space")
    else:
        print("Other")
main()
