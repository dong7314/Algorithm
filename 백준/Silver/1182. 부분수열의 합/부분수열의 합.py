N, S = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << N):
    sum = 0
    for j in range(N):
        if i < 2**j:
            break
        else:
            if i & 2**j:
                sum += arr[j]
    if S == sum:
        cnt += 1

print(cnt)