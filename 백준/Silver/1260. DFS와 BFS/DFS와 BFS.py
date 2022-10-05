def dfs(v):
    visited_d[v] = 1
    print(v, end = ' ')
    for i in range(len(arr[v])):
        if visited_d[arr[v][i]] == 0:
            dfs(arr[v][i])

def bfs(v):
    queue = []
    queue.append(v)
    visited_b[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(len(arr[v])):
            if visited_b[arr[v][i]] == 0:
                queue.append(arr[v][i])
                visited_b[arr[v][i]] = 1



N, M, V = map(int, input().split())
arr = [[] * (N + 1) for _ in range(N + 1)]
visited_d = [0] * (N + 1)
visited_b = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(len(arr)):
    arr[i].sort()

dfs(V)
print()
bfs(V)