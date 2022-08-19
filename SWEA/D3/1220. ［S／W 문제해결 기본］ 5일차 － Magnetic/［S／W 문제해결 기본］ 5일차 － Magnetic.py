T = 10
for tc in range(1, T + 1):
    SIZE = int(input())
    arr = [list(map(int, input().split())) for _ in range(SIZE)]

    flag = 1        # while문 탈출 조건
    while flag:
        flag = 0  # 우선 flag를 0으로 해서 while을 탈출시키는 조건으로 변경
        for i in range(SIZE):
            for j in range(SIZE):
                # i + 1을 범위 밖으로 벗어나지 않게 지정해주고
                # arr[i][j]가 N극의 여부를 판별, N극 아래에 0이라면 한칸 이동시켜준다.
                if i + 1 < 100 and arr[i][j] == 1 and arr[i + 1][j] == 0:
                    arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                    # while을 탈출시키지 않게 한다.
                    flag = 1
                # 위와 동일. S극으로 조건 지정
                elif i - 1 >= 0 and arr[i][j] == 2 and arr[i - 1][j] == 0:
                    arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]
                    flag = 1

    # N극 옆에 S극이 있다면 교착상태라 판별하고
    # cnt 값을 1 증가 시킨다.
    cnt = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if i + 1 < 100 and arr[i][j] == 1 and arr[i + 1][j] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')

