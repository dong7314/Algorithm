T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    base64 = list(input())
    encoding_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    bin_str = ''
    alter_str = ''

    # base64에 담은 문자열리스트를 하나씩 뽑아낸다.
    for value in base64:
        # 받은 문자를 인코딩을 통해 숫자로 변경
        encoding_num = encoding_list.find(value)
        # 10진수를 2진수로 변경
        bin_num = bin(encoding_num)[2:]
        # 2진수를 6자리로 변경하여 bin_str에 추가한다.
        bin_str += '0'*(6-len(bin_num)) + bin_num


    bin8 = ''
    for i in bin_str:
        bin8 += i
        # 만약 bin8이 8개가 되었을 때
        if len(bin8) == 8:
            # 10진수로 변환후
            num = int('0b' + bin8, 2)
            # 그 값을 아스키코드로 변환하여 alter_str에 담는다.
            alter_str += chr(num)
            bin8 = ''

    print(f'#{test_case} {alter_str}')