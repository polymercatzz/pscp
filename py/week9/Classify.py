"""Classify"""
def main():
    """Classify"""
    class_id = []
    result = {}
    while True:
        id_ = input()
        if id_ == "END":
            break
        else:
            class_id.append(id_)
    class_id.sort()
    for i in class_id:
        result[i[:4]] = result.get(i[:4], 0) + 1
    class_id = list(result)
    for i, id_ in enumerate(class_id):
        if class_id[i][:2] == class_id[i-1][:2]:
            print("--", int(id_[2:4]), result.get(id_))
        else:
            print(id_[:2], int(id_[2:4]), result.get(id_))
main()
