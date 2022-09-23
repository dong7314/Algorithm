'''
1
1010
212
'''
def c_binary(arr):
    result = 0
    length = len(arr) - 1
    for i in range(len(arr)):
        if arr[i]:
            result += 2 ** (length - i)
    return result

def c_ternary(arr):
    result = 0
    length = len(arr) - 1
    for i in range(len(arr)):
        if arr[i]:
            result += (3 ** (length - i)) * arr[i]
    return result

def checking(b, t):

    for i in range(len(b)):
        c_b = b[:]
        if i == 0:
            continue

        if c_b[i] == 1:
            c_b[i] = 0
        else:
            c_b[i] = 1
        b_decimal = c_binary(c_b)

        for j in range(len(t)):
            c_t = t[:]
            if j == 0:
                if c_t[j] == 1:
                    c_t[j] = 2
                else:
                    c_t[j] = 1
                t_decimal = c_ternary(c_t)
                if b_decimal == t_decimal:
                    return t_decimal
            else:
                for k in range(3):
                    if c_t[j] != k:
                        c_t[j] = k
                    t_decimal = c_ternary(c_t)
                    if b_decimal == t_decimal:
                        return t_decimal

T = int(input())
for tc in range(1, T + 1):
    b = list(map(int, input()))
    t = list(map(int, input()))

    print(f'#{tc} {checking(b, t)}')


