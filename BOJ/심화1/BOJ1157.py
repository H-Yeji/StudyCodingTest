import collections

s = input().upper()
a = collections.Counter(s)
values = [i for i in a.values()]
values.sort(reverse=True)
max_values = values[0]

result = [i for i, k in a.items() if max_values == k]
result = ''.join(sorted(result))
if len(result) == 1:
    print(result)
else:
    print("?")

