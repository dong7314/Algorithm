T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lines = int(input())
    building_lst = list(map(int, input().split()))
    building = [[0 for _ in range(255)]for _ in range(lines)]
    for i in range(len(building)):
        for j in range(building_lst[i]):
            building[i][j] = 1

    count = 0
    for i in range(len(building)):
        for j in range(building_lst[i]):
            if not(building[i - 1][j] or building[i - 2][j] or building[i + 1][j] or building[i + 2][j]):
                count += 1
    print(f'#{test_case} {count}')