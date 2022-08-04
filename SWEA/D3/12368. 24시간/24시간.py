T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    time1, time2 = map(int, input().split())
    time = time1 + time2
    if time > 23:
        time -= 24
    print(f'#{test_case} {time}')