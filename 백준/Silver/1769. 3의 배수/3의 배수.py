N = input()

cnt = 0
while len(N) >= 2:
    cnt += 1
    sum = 0
    for n in N:
        sum += int(n)
    N = str(sum)

print(cnt)
if int(N) % 3 == 0:
    print('YES')
else:
    print('NO')