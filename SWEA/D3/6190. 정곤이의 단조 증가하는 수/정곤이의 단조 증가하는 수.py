T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    danjo = []

    for i in range(N):
        for j in range(i + 1, N):
            number = arr[i] * arr[j]
            units = number % 10
            flag = 1
            while number:
                number //= 10
                if units < number % 10:
                    flag = 0
                units = number % 10
            if flag == 1:
                danjo.append(arr[i] * arr[j])

    if len(danjo) == 0:
        danjo.append(-1)

    max_danjo = danjo[0]
    for num in danjo:
        if num > max_danjo:
            max_danjo = num

    print(f'#{tc} {max_danjo}')