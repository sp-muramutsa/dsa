def job_sequencing(profits, deadlines):
    """
    Greedy method
    - sort the jobs in descending order of most profitable
    """

    jobs = list(zip(profits, deadlines))
    jobs.sort(key=lambda x: x[0], reverse=True)
    max_deadline = max(deadlines)
    slots = [False] * max_deadline
    max_profit = 0

    for profit, deadline in jobs:
        for i in range(deadline - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                max_profit += profit
                break
    
    print(slots, max_profit)
    print("\n")

job_sequencing([20, 15, 10, 5, 1], [2, 2, 1, 3, 3])
job_sequencing([35, 30, 25, 20, 15, 12, 5], [3, 4, 4, 2, 3, 1, 2])