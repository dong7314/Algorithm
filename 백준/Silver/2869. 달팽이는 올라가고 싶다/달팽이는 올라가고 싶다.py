import math

A, B, V = map(int, input().split())

cnt = 1
V -= A
day = math.ceil(V / (A - B))
cnt += day

print(cnt)
        
