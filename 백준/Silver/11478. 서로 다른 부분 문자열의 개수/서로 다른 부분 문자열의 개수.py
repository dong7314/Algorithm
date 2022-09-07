str_list = list(input())

N = len(str_list)
str_set = set()
for i in range(1, N + 1):
    for j in range(N + 1 - i):
        arr = str_list[j:j+i]
        str_set.add(''.join(arr))

print(len(str_set))
