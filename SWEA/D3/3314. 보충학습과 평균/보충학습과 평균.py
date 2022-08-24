T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    total = 0
    for i in range(len(arr)):
        # 만약 점수가 40점 미만이라면 total에 40을 더한다
        if arr[i] < 40:
            total += 40
        else:
            total += arr[i]

    avg = int(total / len(arr))
    print(f'#{tc} {avg}')
