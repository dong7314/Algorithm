import math

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    # 카운트 개수
    count = 0
    # 근을 담는 리스트
    sqrt_list = [float(i) for i in range(int(math.sqrt(B)) + 1)]
    # A 와 B 사이를 for로 반복
    for i in range(A, B + 1):
        # 주어진 수를 문자열로 변경 후 회문을 통해 확인
        str_i = str(i)
        if str_i == str_i[::-1]:
            # 근이 sqrt_list에 담겨있다면
            if math.sqrt(i) in sqrt_list:
                # 근을 다시 회문을 통해 확인 후 count에 1을 추가한다.
                if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
                    count += 1

    print(f'#{test_case} {count}')
