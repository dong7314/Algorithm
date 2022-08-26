def abs(num):
    if num < 0:
        return -num
    else:
        return num

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            d = 1
            if i > N // 2:
                d = -3
            if abs(N // 2 - i) <= j <= abs(d * (N // 2) + i):
                cnt += arr[i][j]

    print(f'#{tc} {cnt}')