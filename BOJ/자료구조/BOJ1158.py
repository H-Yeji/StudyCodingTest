import sys
input = sys.stdin.readline


def josephus(n, k):
    people = [i for i in range(1, n + 1)]
    result = []
    idx = 0

    while people:
        idx = (idx + k - 1) % len(people)
        result.append(people.pop(idx))
    return result


n, k = map(int, input().split())
result = josephus(n, k)
print("<" + ", ".join(map(str, result)) + ">")
