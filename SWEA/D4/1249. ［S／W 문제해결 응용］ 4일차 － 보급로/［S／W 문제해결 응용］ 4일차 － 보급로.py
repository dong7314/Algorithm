'''
1
4
0100
1110
1011
1010
'''
def dijkstra(x, y):
    D[x][y] = 0

    for _ in range(N * N):
        min_value = INF
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and D[i][j] < min_value:
                    min_value = D[i][j]
                    x, y = i, j

        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if D[nx][ny] > D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 987654321
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[-1][-1]}')