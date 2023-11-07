"""Pad Thai"""
def main():
    """Pad Thai"""
    allmenu = {"Pad Thai Sauce", 'Tofu', 'Pickle Turnip', 'Shrimp', \
            'Bean Sprouts', 'Noodle', 'Chives', 'Lime', 'Egg', 'Oil', 'Peanuts'}
    alltaste = {"Sweet", "Sour", "Salty"}
    result = []
    while True:
        word = input()
        if word == "End":
            break
        result.append(word)
    menu = result[:result.index("Cook")]
    taste = result[result.index("Cook")+1:]
    if set(menu)-allmenu:
        print("This is not Pad Thai!!!")
    elif allmenu-set(menu):
        print("This is bad!")
    elif set(taste)-alltaste != alltaste-set(taste):
        print("Not Bad...")
    else:
        print("Delicious!")
main()
