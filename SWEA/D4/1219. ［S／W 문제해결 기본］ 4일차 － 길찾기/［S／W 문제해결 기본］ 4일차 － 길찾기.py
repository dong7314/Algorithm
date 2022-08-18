def route(s, g):
    if len(arr[s]) == 0:
        return 0

    for num in arr[s]:
        if num == g:
            return 1
        if route(num, g) == 1:
            return 1

    return 0

T = 10
for tc in range(1, T + 1):
    TC, V = map(int, input().split())

    arr = [[] for _ in range(100)]
    temp = list(map(int, input().split()))
    for i in range(V):
        r1, r2 = temp[2 * i], temp[2 * i + 1]
        arr[r1].append(r2)

    result = route(0, 99)
    print(f'#{tc} {result}')