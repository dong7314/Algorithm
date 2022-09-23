def comb(n, r, k, s):
    global min_V
    if k == r:
        team1 = []
        team2 = []
        for i in range(1, N + 1):
            if i in p:
                team1.append(i)
            else:
                team2.append(i)
        score1 = 0
        score2 = 0
        for i in range(R - 1):
            for j in range(i + 1, R):
                score1 += capacity[team1[i] - 1][team1[j] - 1] + capacity[team1[j] - 1][team1[i] - 1]
                score2 += capacity[team2[i] - 1][team2[j] - 1] + capacity[team2[j] - 1][team2[i] - 1]
        if abs(score1 - score2) < min_V:
            min_V = abs(score1 - score2)
    else:
        for i in range(s, n - r + 1 + k):
            p[k] = a[i]
            comb(n, r, k + 1, i + 1)

N = int(input())
capacity = [list(map(int, input().split())) for _ in range(N)]
R = N // 2
a = [i for i in range(1, N + 1)]
p = [0] * R
visited = [0] * N
min_V = 987654321

comb(N, R, 0, 0)

print(min_V)
