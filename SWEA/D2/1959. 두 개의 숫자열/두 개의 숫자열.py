T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 만약 N 값이 M보다 크다면 둘의 위치를 변경하기
    if N > M:
        N, M = M, N
        A, B = B, A

    # 최대값을 담을 변수
    max_total = 0
    # N의 리스트 위치를 한자리 씩 옆으로 옮겨주는 변수
    k = 0
    # M의 크기에 따라 N을 옮겨줄 때 돌려주는 for문의 최대 개수
    for i in range(M - N + 1):
        total = 0
        # 맞춰준 자리에 따라 곱한 후 total에 추가
        for j in range(N):
            total += A[j] * B[j + k]
        # 만약 total이 max_total보다 크다면 최대값 변경
        if total > max_total:
            max_total = total
        # N 자리를 옆으로 한칸 이동시켜준다.
        k += 1

    print(f'#{test_case} {max_total}')
