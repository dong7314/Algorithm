import copy
from collections import deque
import copy

def setting(c):
    global ans
    if c == 3:
        c_arr = copy.deepcopy(arr)
        queue = deque()
        for k in range(N):
            for l in range(M):
                if c_arr[k][l] == 2:
                    queue.append((k, l))

        while queue:
            x, y = queue.popleft()
            for m in range(4):
                nx = x + dx[m]
                ny = y + dy[m]
                if 0 <= nx < N and 0 <= ny < M:
                    if c_arr[nx][ny] == 0:
                        c_arr[nx][ny] = 2
                        queue.append((nx, ny))
        cnt = 0
        for i in range(N):
            for j in range(M):
                if c_arr[i][j] == 0:
                    cnt += 1
        if cnt > ans:
            ans = cnt
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    setting(c + 1)
                    arr[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

setting(0)

print(ans)