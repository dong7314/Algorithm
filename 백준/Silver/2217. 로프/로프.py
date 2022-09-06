N = int(input()) # 총 개수

arr = [int(input()) for _ in range(N)]
weight = []
arr.sort()
n = 1
while n <= N: # n이 총 개수보다 커질 때
    max_arr = arr[N - n]
    weight.append(max_arr * n)
    n += 1
print(max(weight))