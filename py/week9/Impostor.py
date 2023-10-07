"""Impostor"""
import json
def main():
    """Impostor"""
    count = 0
    people = {}
    people_died = {}
    while True:
        word = input()
        if word == "Start":
            break
        people.update(json.loads(word))
    people = dict(sorted(list(people.items())))
    while True:
        word = input()
        if word == "End":
            break
        people_died.update({word:people.pop(word)})
    people_died = dict(sorted(list(people_died.items())))
    for i in people.values():
        if i == "Impostor":
            count += 1
    print("%d Impostor Remains"%count)
    print("***Alive***")
    for key, value in people.items():
        print(key, value, sep=" : ")
    print("***Dead***")
    for key, value in people_died.items():
        print(key, value, sep=" : ")
main()
