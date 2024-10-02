n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

dp = [0] * n
if len(array) <= 2:
    print(sum(array))
else:
    dp[0] = array[0]
    dp[1] = array[0] + array[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + array[i - 1] + array[i], dp[i - 2] + array[i])
    print(dp[-1])