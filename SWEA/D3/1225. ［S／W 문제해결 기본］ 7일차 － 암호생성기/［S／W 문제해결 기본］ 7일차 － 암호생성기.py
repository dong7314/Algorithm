T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = input()
    pw_list = list(map(int, input().split()))

    n = 1
    while True: # do while문과 같이 사용하려고 함
        # n이 6이 되면 n을 1로 초기화
        if n == 6:
            n = 1
        # pw_list에서 첫 번째 값을 뽑아낸 후 n만큼 빼서 pw_num 변수에 담는다.
        pw_num = pw_list.pop(0) - n
        # 무한 루프 탈출 조건으로 pw_num이 0이하가 되면
        # pw_list 마지막에 0을 추가하고 루프 탈출
        if pw_num <= 0:
            pw_list.append(0)
            break
        # n만큼 뺀 값을 다시 pw_list 마지막에 담는다
        pw_list.append(pw_num)
        n += 1
        
    pw_list = ' '.join(map(str, pw_list))
    print(f'#{test_case} {pw_list}')