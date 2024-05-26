import random
hash_table = [0 for i in range(11)]


def save(key, value):
    index = hash(key) % len(hash_table)

    # index(key 주소)부터 hash_table 끝까지 선형 탐색
    for i in range(index, len(hash_table)):
        # 빈공간이면
        if hash_table[i] == 0:
            hash_table[i] = [key, value]
            return

        # 빈 공간이 아니고 데이터의 key값이 같다면
        elif hash_table[i][0] == key:
            hash_table[i][1] = value
            return


key_candidates = ['a','b','c','d','e','f','g','h']
for i in range(7):
    save(key_candidates[i], random.randint(1,11))

print(hash_table)
