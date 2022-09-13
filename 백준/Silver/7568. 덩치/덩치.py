N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    ranking = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            ranking += 1
    print(ranking + 1, end=' ')