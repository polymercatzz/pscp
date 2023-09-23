"""OneTwo"""
def main(num):
    """OneTwo"""
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    return main(num-1)+main(num-2)
print(main(int(input())))
