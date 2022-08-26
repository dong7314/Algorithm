T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hallway = [0] * 200

    for i in range(N):

        if arr[i][0] % 2 == 0:
            idx1 = arr[i][0] // 2 - 1
        else:
            idx1 = arr[i][0] // 2

        if arr[i][1] % 2 == 0:
            idx2 = arr[i][1] // 2 - 1
        else:
            idx2 = arr[i][1] // 2

        if idx1 >= idx2:
            for j in range(idx2, idx1 + 1):
                hallway[j] += 1
        else:
            for j in range(idx1, idx2 + 1):
                hallway[j] += 1

    time = 0
    for i in range(200):
        if hallway[i] > time:
            time = hallway[i]

    print(f'#{tc} {time}')
