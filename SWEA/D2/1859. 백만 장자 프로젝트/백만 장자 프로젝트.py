T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    lst = list(map(int, input().split()))
    lst_num = len(lst) - 1

    total = 0
    last_num = lst.pop()
    while lst_num > 0:
        next_num = lst.pop()
        if next_num < last_num:
            total += last_num - next_num
        else:
            last_num = next_num
        lst_num -= 1
    print(f'#{test_case} {total}')
