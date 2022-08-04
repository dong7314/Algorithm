T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    divisors_list = [2, 3, 5, 7, 11] # 약수들의 리스트
    square_number_list = [] # 제곱수를 담을 리스트

    # 약수 리스트를 for문으로 통해 순환
    for divisor in divisors_list:
        # count는 제곱수의 갯수
        count = 0
        # 만약 주어진 number가 약수로 나누어지지 않는다면 break
        while number % divisor == 0:
            number /= divisor
            count += 1
        square_number_list.append(count)
    
    # 출력문
    print(f'#{test_case}', end=' ')
    for n in square_number_list:
        print(n, end=' ')
    print()