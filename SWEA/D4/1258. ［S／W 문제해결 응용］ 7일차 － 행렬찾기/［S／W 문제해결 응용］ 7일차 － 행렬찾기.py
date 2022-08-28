T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    c_dict = {}
    for i in range(N):
        row = 0
        for j in range(N):
            if arr[i][j] != 0:
                row += 1
            else:
                if row > 0:
                    c_dict[row] = c_dict.get(row, 0) + 1
                row = 0
            if j == N - 1 and row > 0:
                c_dict[row] = c_dict.get(row, 0) + 1

    cnt = 0
    k = []
    for i in c_dict.keys():
        cnt += 1
        k.append((c_dict[i], i))

    for i in range(len(k)):
        min_value = 0
        value = k[i][0] * k[i][1]
        for j in range(i + 1, len(k)):
            if k[j][0] * k[j][1] < value:
                k[i], k[j] = k[j], k[i]
                value = k[i][0] * k[i][1]
            elif k[j][0] * k[j][1] == value:
                if k[j][0] < k[i][0]:
                    k[i], k[j] = k[j], k[i]

    print(f'#{tc} {cnt}', end=' ')
    for n in k:
        print(n[0], n[1], end=' ')
    print()

