"""[Midterm 2020] BigFrame"""
def main():
    """[Midterm 2020] BigFrame"""
    word_1 = input().strip()
    word_2 = input().strip()
    word_3 = input().strip()
    word_4 = input().strip()
    word_5 = input().strip()
    word_more = max(len(word_1), len(word_2), len(word_3), len(word_4), len(word_5))
    print("**"+"*"*word_more+"**")
    print("* "+word_1+" "*(word_more-len(word_1))+" *")
    print("* "+word_2+" "*(word_more-len(word_2))+" *")
    print("* "+word_3+" "*(word_more-len(word_3))+" *")
    print("* "+word_4+" "*(word_more-len(word_4))+" *")
    print("* "+word_5+" "*(word_more-len(word_5))+" *")
    print("**"+"*"*word_more+"**")
main()
