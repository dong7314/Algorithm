T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    for i in range(1, 1 << N):
        sum = 0
        for j in range(N):
            if i & 2**j:
                sum += arr[j]
        if sum >= B:
            result.append(sum)

    print(f'#{tc} {min(result) - B}')
