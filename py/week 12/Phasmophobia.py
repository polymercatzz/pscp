"""Phasmophobia"""
def main(word1, word2, word3):
    """Phasmophobia"""
    result = set()
    ghost = {"EMF Level 5":["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"], \
            "Ghost Writing":["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"], \
            "Fingerprints":["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"], \
            "Spirit Box":["Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"], \
            "Freezing Temperatures":["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"], \
            "Ghost Orb":["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"]}
    result = ["Banshee", "Demon", "Jinn", "Oni", "Phantom", "Revenant", "Shade", "Mare", \
            "Poltergeist", "Wraith", "Yurei", "Spirit"]
    result = set(ghost.get(word1, result)) & set(ghost.get(word2, result)) & \
            set(ghost.get(word3, result))
    if result == set():
        result.add("Not yet discovered")
    result = sorted(list(result))
    print(*result, sep="\n")
main(input(), input(), input())
