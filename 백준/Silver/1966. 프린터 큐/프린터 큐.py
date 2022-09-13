T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0] * 1000000

    for i in range(N):
        if i == M:
            queue[i] = -1
            queue[i + 1] = arr[i]
        elif i > M:
            queue[i + 1] = arr[i]
        else:
            queue[i] = arr[i]

    rear = 0
    front = N + 1
    cnt = 0
    while True:
        max_v = max(arr)
        if queue[rear] == max_v:
            cnt += 1
            arr.remove(max_v)
            if queue[front - 1] == -1:
                break
            rear += 1
        else:
            queue[front] = queue[rear]
            rear += 1
            front += 1

    print(cnt)



