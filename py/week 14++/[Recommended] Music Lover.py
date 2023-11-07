"""[Recommended] Music Lover"""
def main(num):
    """[Recommended] Music Lover"""
    song = {}
    for _ in range(num):
        music = input().split("-")
        song[music[0]] = song.get(music[0], [])+[music[1]]
    for key, value in song.items():
        print(key, *value, sep="\n")
main(int(input()))
