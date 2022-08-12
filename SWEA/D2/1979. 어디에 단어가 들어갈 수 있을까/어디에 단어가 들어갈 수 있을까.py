# import sys; sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 가로 기준으로 리스트로 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 세로 기준으로 리스트 변경
    arr_column = list(zip(*arr))

    # 총 카운트 갯수
    cnt = 0
    for i in range(N):
        # 연속을 세는 변수
        cn_row = 1
        cn_column = 1
        for j in range(N-1):
            # 가로
            # 만약 현재 인덱스와 다음번 인덱스가 1이라면
            if arr[i][j] == arr[i][j + 1] == 1:
                # cn_row 변수를 1 증가
                cn_row += 1
                # 마지막 인덱스에 도달했을 때 연속되어 있으며
                # cn_row 갯수가 K와 같다면 cnt 1증가
                if j == N - 2:
                    if cn_row == K:
                        cnt += 1
            else:
                # 연속되지 않았을 때
                # 만약 이제 까지 연속된 횟수가 K와 같다면 cnt 1증가
                if cn_row == K:
                    cnt += 1
                # 연속 횟수 초기화
                cn_row = 1
            
            # 세로
            if arr_column[i][j] == arr_column[i][j + 1] == 1:
                cn_column += 1
                if j == N - 2:
                    if cn_column == K:
                        cnt += 1
            else:
                if cn_column == K:
                    cnt += 1
                cn_column = 1

    print(f'#{tc} {cnt}')

