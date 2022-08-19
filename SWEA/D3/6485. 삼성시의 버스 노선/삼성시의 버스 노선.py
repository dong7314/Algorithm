T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    P_list = [int(input()) for _ in range(P)]

    # 정류장에 다니는 노선의 개수를 담을 리스트
    count = [0] * (5001)
    for i in range(len(arr)):
        for j in range(arr[i][0], arr[i][1] + 1):
            # Ai ~ Bi 정류장 번호마다 count에 1씩 추가
            count[j] += 1

    print(f'#{tc}', end=' ')
    for p in P_list:
        print(count[p], end=' ')
    print()