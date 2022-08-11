T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    vector = [-1, 1]
    present_vec = 0

    for start in range(100):
        if arr[0][start] == 1: # 첫 줄 인덱스의 값이 1이면 시작
            i, j = 0, start
            while i != 99:
                # 현재 방향이 왼쪽, 오른쪽일 때
                if present_vec != 0:
                    if 0 <= j + present_vec < 100 and arr[i][j + present_vec] == 1:
                        j += present_vec
                    else:
                        present_vec = 0
                # 현재 방향이 아래일 때
                else:
                    i += 1
                    present_vec = 0
                    # 좌우 값들을 확인
                    for v in vector:
                        nj = j + v
                        if 0 <= nj < 100:
                            if arr[i][nj] == 1:
                                present_vec = v
            if arr[99][j] == 2:
                print(f'#{test_case} {start}')
