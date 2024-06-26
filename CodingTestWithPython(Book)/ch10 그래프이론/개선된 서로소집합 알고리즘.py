# 특정 원소가 속한 집합 찾기 (경로 압축)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모를 자기 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()
# 부모 테이블 출력
for i in range(1, v + 1):
    print(parent[i], end=' ')
