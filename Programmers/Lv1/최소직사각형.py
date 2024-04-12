import sys
input = sys.stdin.readline


def solution(sizes):
    for i, num in enumerate(sizes):
        if num[0] < num[1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_w, max_h = 0, 0
    for w, h in sizes:
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h

    return max_w * max_h


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
