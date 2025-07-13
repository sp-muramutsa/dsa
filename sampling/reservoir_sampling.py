import random

def reservoir_sampling(data: list, k: int) -> list:
    """
    Picks k random samples with equal probability when the algorithm does not know the length of the data.
    In short, it works on the fly. 

    Returns a list of k sampled elements.
    """

    reservoir = []

    for iterator, value in enumerate(data):
        # Step 1: Put the first k elements in the reservoir
        if iterator < k:
            reservoir.append(data[iterator])
        
        # Step 2: Iterate till the end, replacing elements with the probability P(replacement) = iterator / k
        else:
            # Pick a random index in the range 0 to iterator for replacement
            idx = random.randint(0, iterator)
            if idx < k:
                reservoir[idx] = data[iterator]
    
    return reservoir



data = range(100)
k = 10
print(reservoir_sampling(data, k))
