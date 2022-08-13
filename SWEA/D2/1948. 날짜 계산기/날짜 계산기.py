T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    
    # 달의 일수들을 계속해서 더한 배열
    day_arr = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    # 전 달의 총 일수 더하기 현재 일을 뺀 값에서 1을 더했다.
    cnt = (day_arr[arr[2] - 1] + arr[3]) - (day_arr[arr[0] - 1] + arr[1]) + 1

    print(f'#{test_case} {cnt}')