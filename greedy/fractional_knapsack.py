def fractional_knapsack(profits: list[float], weights: list[float], capacity: float) -> float:
    """
    Calculates the maximum profit using the Greedy Method
    """

    items = list(zip(profits, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    print(items)
    
    remaining_capacity = capacity
    max_profit = 0
    n = len(profits)

    i = 0
    for i in range(n):
        if items[i][1] <= remaining_capacity:
            max_profit += items[i][0]
            remaining_capacity -= items[i][1]
        
        else:
            max_profit += (remaining_capacity / items[i][1]) * items[i][0]
            break
    
    print("Max profit: ", max_profit, end="\n\n")

fractional_knapsack([10, 5, 15, 7, 6, 18, 3], [2, 3, 5, 7, 1, 4, 1], 15)
fractional_knapsack([60, 100, 120], [10, 20, 30], 50)