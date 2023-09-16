"""ValidVar"""
def main():
    """ValidVar"""
    num = int(input())
    reserved = ["if", "else", 'elif', 'while', 'for', 'True', 'False', \
            'continue', 'break', 'return', 'is', 'in', 'and', 'or', \
            'from', 'as', 'pass', 'not', 'def', 'None']
    for word in range(num):
        result = "Valid"
        word = input()
        for i in word:
            if not i.isalnum() and i != "_":
                result = "Invalid"
        if word.isspace() or word[0].isnumeric():
            result = "Invalid"
        for i in reserved:
            if i == word:
                result = "Invalid"
                break
        print(result)
main()
