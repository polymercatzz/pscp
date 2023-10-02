"""BookWorm"""
def main(exam):
    """BookWorm"""
    result = []
    for _ in range(exam):
        time = float(input())
        book = int(input())
        time_read = []
        for _ in range(book):
            time_read.append(float(input()))
        time_read.sort()
        for i in range(len(time_read), -1, -1):
            total = sum(time_read[:i])
            if total <= time:
                result.append(i)
                break
    print(*result, sep="\n")
main(int(input()))
