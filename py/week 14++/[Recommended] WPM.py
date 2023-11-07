"""[Recommended] WPM"""
def main(age, wpm):
    """[Recommended] WPM"""
    kid = {10:'Very Slow', 20:'Slow', 30:'Average', 40:'Fast'}
    adult = {25:'Very Slow', 35:'Slow/Beginner', 45:'Intermediate/Average',\
            65:'Fast/Advanced', 80:'Very Fast'}
    if age == "Kids":
        for key, value in kid.items():
            if wpm <= key:
                print(value)
                break
            if key == 40:
                print("Very Fast")
    else:
        for key, value in adult.items():
            if wpm <= key:
                print(value)
                break
            if key == 80:
                print("Insane")
main(input(), int(input()))
