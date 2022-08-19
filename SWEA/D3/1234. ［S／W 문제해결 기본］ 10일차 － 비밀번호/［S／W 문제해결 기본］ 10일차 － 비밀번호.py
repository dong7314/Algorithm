T = 10
for tc in range(1, T + 1):
    N, str1 = input().split()
    N = int(N)
    str1 = list(str1)

    flag = 1        # flag를 1로 잡아 while문을 실행
    while flag:
        flag = 0    # flag를 0으로 초기화
        for i in range(len(str1) - 1):
            # 만약 if 문이 실행되지 않는다면 while문 종료
            if str1[i] == str1[i + 1]:
                # 현재 인덱스와 다음 인덱스 값들이 같다면 pop을 통해 두 인덱스 제거
                str1.pop(i + 1)
                str1.pop(i)
                flag = 1    # flag에 1을 담아 while문 다시 작동
                break

    str1 = ''.join(str1)
    print(f'#{tc} {str1}')
