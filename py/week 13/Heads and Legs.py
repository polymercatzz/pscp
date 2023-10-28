"""Heads and Legs"""
def main(animal, leg):
    """Heads and Legs"""
    rab = (leg-animal*2)//2
    bird = animal-rab
    if rab < 0 or bird < 0 or leg%2 == 1:
        print("Impossible")
    else:
        print(rab, bird)
main(int(input()), int(input()))
