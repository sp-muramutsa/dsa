def unbounded_knapsack(profits, weights, max_weight):
    n = len(profits)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            choose = 0
            if w - weights[i - 1] >= 0:
                choose = profits[i - 1] + dp[i][w - weights[i - 1]]

            not_choose = dp[i - 1][w]
            dp[i][w] = max(choose, not_choose)
    
    print(dp)
    print("Maximum profit: ", dp[-1][-1])

unbounded_knapsack([1, 4, 7, 10], [1, 2, 3, 5], 8)
