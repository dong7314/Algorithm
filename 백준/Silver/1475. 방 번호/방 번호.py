arr = list(map(int, input()))

cnt = 1
visited = [1] * 10
for num in arr:
    if num == 6 or num == 9:
        if visited[6]:
            visited[6] -= 1
        elif visited[9]:
            visited[9] -= 1
        else:
            for i in range(10):
                visited[i] += 1
            visited[6] -= 1
            cnt += 1
    else:
        if visited[num]:
            visited[num] -= 1
        else:
            for i in range(10):
                visited[i] += 1
            visited[num] -= 1
            cnt += 1

print(cnt)