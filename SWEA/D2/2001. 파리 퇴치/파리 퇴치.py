T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += arr[i + k][j + l]
            if total > max_total:
                max_total = total

    print(f'#{tc} {max_total}')
