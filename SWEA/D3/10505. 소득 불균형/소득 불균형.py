T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    income_list = list(map(int, input().split()))

    # 소득의 평균
    income_sum = sum(income_list) / length

    # income_list를 돌려 각각의 income을 가져오고
    # 평균 이하면 count에 1씩 추가
    count = 0
    for income in income_list:
        if income <= income_sum:
            count += 1
    
    print(f'#{test_case} {count}')