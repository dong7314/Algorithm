N = int(input())

max_cnt = 0
max_arr = []
for i in range(N, 0, -1):
    arr = [N, i]
    k = N - i
    while k >= 0:
        arr.append(k)
        k = arr[-2] - arr[-1]
    if len(arr) > max_cnt:
        max_cnt = len(arr)
        max_arr = arr

print(max_cnt)
print(*max_arr)