T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tri = [[0] * i for i in range(1, N + 1)]
    for i in range(N):
        for j in range(len(tri[i])):
            if j == 0 or j == len(tri[i]) - 1:
                tri[i][j] = 1

    for i in range(N):
        for j in range(len(tri[i])):
            if tri[i][j] == 0:
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

    print(f'#{tc}')
    for i in range(N):
        for num in tri[i]:
            print(num, end=' ')
        print()
