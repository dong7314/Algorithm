T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_h = min_h = 0

    while N >= 0:
        for i in range(100):
            if arr[i] > arr[max_h]:
                max_h = i
            elif arr[i] < arr[min_h]:
                min_h = i
        if N == 0:
            break
        arr[max_h] -= 1
        arr[min_h] += 1

        N -= 1

    print(f'#{tc} {arr[max_h] - arr[min_h]}')