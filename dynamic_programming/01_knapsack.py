from typing import List


def knapsack_01(values: List[int], weights: List[int], bag_size: int) -> None:

    # Make a 2D table
    n = len(values)
    dp = [[0] * (bag_size + 1) for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, bag_size + 1):

            # Choose
            choose = 0
            if w >= weights[i - 1]:
                choose = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            # Don't choose
            not_choose = dp[i - 1][w]

            dp[i][w] = max(choose, not_choose)

    # Get maximum possible profit under constraints
    print("Maximum profit that can be made is: ", dp[-1][-1])

    # Determine who got taken and who didn't
    row, col = n, bag_size
    included = [False] * n

    while row > 0 and col > 0:
        if dp[row][col] != dp[row - 1][col]:
            included[row - 1] = True
            col -= weights[row - 1]
        row -= 1

    print("Binary description of inclusion: ", included)
    print("\n")


def knapsack_01_optimized(values: List[int], weights: List[int], bag_size: int) -> None:
    """
    Space: O(n) space
    """

    dp = [0] * (bag_size + 1)
    n = len(values)
    included = [False] * n
    choice = [-1] * (bag_size + 1)

    for i in range(n):
        for w in range(bag_size, weights[i] - 1, -1):
            if dp[w - weights[i]] + values[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + values[i]
                choice[w] = i

    print("Maximum profit that can be made is: ", dp[-1])

    curr_w = bag_size
    while curr_w > 0 and choice[curr_w] != -1:
        chosen_idx = choice[curr_w]
        included[chosen_idx] = True
        curr_w -= weights[chosen_idx]

    print("Binary description of inclusion: ", included)
    print("\n")


knapsack_01([0, 10, 50, 20, 40, 20], [3, 2, 4, 2, 1, 9], 12)
knapsack_01_optimized([0, 10, 50, 20, 40, 20], [3, 2, 4, 2, 1, 9], 12)


knapsack_01([1, 2, 5, 6], [2, 3, 4, 5], 8)
knapsack_01_optimized([1, 2, 5, 6], [2, 3, 4, 5], 8)
