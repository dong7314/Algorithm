def bfs(x, y):
    global flag
    q = []
    q.append((x, y))
    visited[x][y] = 1

    while q:
        i, j = q.pop(0)
        for k in range(4):
            di = i + dx[k]
            dj = j + dy[k]
            if 0 <= di < SIZE and 0 <= dj < SIZE:
                if maze[di][dj] == 3:
                    flag = 1
                if (not visited[di][dj]) and maze[di][dj] == 0:
                    q.append((di, dj))
                    visited[di][dj] = 1

SIZE = 100
T = 10
for tc in range(1, T + 1):
    temp = input()
    maze = [list(map(int, input())) for _ in range(SIZE)]
    visited = [[0] * SIZE for _ in range(SIZE)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if maze[i][j] == 2:
                si, sj = i, j

    bfs(si, sj)

    print(f'#{tc} {flag}')
