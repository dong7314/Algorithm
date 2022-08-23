N = int(input())
arr = [[0] * 1001 for _ in range(1001)]


for k in range(N):
    a, b, x, y = map(int, input().split())

    for i in range(a, a + x):
        for j in range(b, b + y):
            arr[i][j] = 1 + k

result = [0] * N
for k in range(N):
    for m in range(1001):
        for n in range(1001):
            if arr[m][n] == 1 + k:
                result[k] += 1

for i in range(N):
    print(result[i])
