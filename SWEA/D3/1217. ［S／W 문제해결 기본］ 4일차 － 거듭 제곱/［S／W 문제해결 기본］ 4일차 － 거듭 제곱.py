def squared(num, square):
    if square == 1:
        return num
    return num * squared(num, square - 1)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    num1, num2 = map(int, input().split())
    print(f'#{test_case} {squared(num1, num2)}')