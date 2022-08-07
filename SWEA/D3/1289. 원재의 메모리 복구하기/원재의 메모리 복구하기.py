T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()

    # 첫 번째 1의 인덱스 번호를 가져온다.
    index_1 = data.find('1')

    result = 1
    # 찾은 1이 마지막 인덱스일 경우 결과값을 1로 저장
    if index_1 == len(data) - 1:
        result = 1
    else:
        # data를 반복시켜 현재와 다음 인덱스 번호가 다르면 
        # result에 1을 추가 아니면 넘긴다.
        # 시작은 index_1로 지정해 1이 저장된 위치부터 검색한다.
        for i in range(index_1 ,len(data) - 1):
            if data[i] != data[i + 1]:
                result += 1
    
    print(f'#{test_case} {result}')
