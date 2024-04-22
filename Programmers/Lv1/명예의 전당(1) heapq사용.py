import heapq


def solution(k, score):
    min_heap = []
    result = []

    for s in score:
        if len(min_heap) < k:
            heapq.heappush(min_heap, s)
        elif s > min_heap[0]:
            heapq.heapreplace(min_heap, s)

        result.append(min_heap[0])

    return result


k = 3
scores = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, scores))
