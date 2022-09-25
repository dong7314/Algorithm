def moduler(A, B):
    if B == 1:
        return A % C

    temp = moduler(A, B // 2)

    if B % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * A % C

A, B, C = map(int, input().split())
print(moduler(A, B))