# import sys
# sys.stdin = open('txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    K = 1

    # 1의 자리로 바꾼 뒤 저장할 세트
    num_set = set()
    # 0~9까지 저장되어 있는 세트
    one_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    while True:
        number = K * N
        # 1의 자리로 변경 후 num_set에 저장한다.
        while number > 0:
            num_set.add(number % 10)
            number //= 10
        # 만약 num_set이 0~9까지 저장되었다면 멈춘다.
        if num_set == one_set:
            break
        K += 1

    print(f'#{test_case} {K * N}')

