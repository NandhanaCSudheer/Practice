n = int(input())
coins = list(map(int,input().split()))
amt = int(input())

dp = [float('inf')] * (amt + 1)
dp[0] = 0

for i in range(1,amt + 1):
    for j in coins:
        if j <= i:
            dp[i] = min(dp[i],dp[i - j] + 1)

if dp[amt] == float('inf'):
    print(-1)
else:
    print(dp[amt])