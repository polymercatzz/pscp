"""Parallelogram"""
def main(text):
    """Parallelogram"""
    num = 1
    for i in range(-len(text)+1, len(text)):
        if i < 0:
            print(" "*abs(len(text)-num)+text[0:num])
            num += 1
        elif i >= 0:
            print(text[abs(i):])
main(input())
