from collections import deque

def bfs(i, j, t):
    queue = deque()
    t.append(arr[i][j])
    queue.append((i, j, t))
    while queue:
        i, j, temp = queue.popleft()
        if len(temp) == 7:
            result_set.add(tuple(temp))
        else:
            for k in range(4):
                c_temp = temp[:]
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    c_temp.append(arr[ni][nj])
                    queue.append((ni, nj, c_temp))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N = 4
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_set = set()

    for i in range(N):
        for j in range(N):
            bfs(i, j, [])

    print(f'#{tc} {len(result_set)}')