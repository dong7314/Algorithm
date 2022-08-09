# import sys
# sys.stdin = open('txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    A_fee = P * W
    B_fee = Q if W < R else Q + S * (W - R)

    result = A_fee if A_fee < B_fee else B_fee

    print(f'#{test_case} {result}')

