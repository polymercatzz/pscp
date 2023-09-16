"""Sequence X"""
def main():
    """Sequence X"""
    num = int(input())
    for _ in range(1, num+1):
        word = 1
        for i in range(num, 0, -1):
            if i <= _:
                print("%02d" %word, end=" ")
                word += 1
            else:
                print("  ", end=" ")
        word_2 = word-2
        for num_1 in range(num, 0, -1):
            if num_1 < _:
                print("%02d" %word_2, end=" ")
                word_2 -= 1
        print()
    for _ in range(num-1, 0, -1):
        word = 1
        for i in range(num, 0, -1):
            if i <= _:
                print("%02d" %word, end=" ")
                word += 1
            else:
                print("  ", end=" ")
        word_2 = word-2
        for num_1 in range(num, 0, -1):
            if num_1 < _:
                print("%02d" %word_2, end=" ")
                word_2 -= 1
        print()
main()
