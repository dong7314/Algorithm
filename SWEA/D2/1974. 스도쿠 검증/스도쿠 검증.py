T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 1~9까지 담은 set
    num_set = {i for i in range(1, 10)}

    flag = 1
    for i in range(9):
        # 세로 방향 세트
        column = set()
        for j in range(9):
            # 블럭 방향 세트
            block = set()
            # 세로 방향에 값들을 추가한다.
            column.add(sudoku[j][i])
            if i % 3 == 0 and j % 3 == 0:
                for k in range(9):
                    # 만약 i, j = 0이라면 i와 j가 0 1 2만 돌도록 세팅
                    # j가 3라면 i는 0 1 2 j는 3 4 5
                    block.add(sudoku[i + k // 3][j + (k % 3)])
                # block에 다 채우고 판별한다.
                if block != num_set:
                    flag = 0
        # 가로 방향 판단
        if set(sudoku[i]) != num_set:
            flag = 0
        # 세로 방향 판단
        elif column != num_set:
            flag = 0

    print(f'#{tc} {flag}')