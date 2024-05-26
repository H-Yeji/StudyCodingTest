import random
hash_table = [0 for i in range(11)]


def save(key, value):
    index = hash(key) % len(hash_table) # 임의의 해시함수

    # 찾아간 index가 비어있지 않다면 (=숫자 존재)
    if hash_table[index] != 0:
        # 같은 key값 있는지 확인
        for data in hash_table[index]:
            if data[0] == key:
                data[1] = value
                return

        # 같은 key값이 없다면
        # 해당 index에 이어서 append하기 (연결리스트 형태)
        return hash_table[index].append([key, value])

    # 찾아간 index가 비어있다면 해당 위치에 key와 value 넣어주기
    hash_table[index] = [[key, value]]
    return


key_candidates = ['a','b','c','d','e','f','g','h']
for i in range(7):
    save(key_candidates[i], random.randint(1,11))

print(hash_table)