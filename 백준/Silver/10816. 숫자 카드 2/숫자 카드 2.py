N = int(input())
Card = list(map(int, input().split()))
M = int(input())
Num = list(map(int, input().split()))
result = [0] * 20000001

for i in range(N):
    result[Card[i]] += 1

for i in range(M):
    print(result[Num[i]], end=' ')
