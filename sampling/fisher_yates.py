import random

class FisherYatesRandom:
    """
    Fisher-Yates algorithm for generating random numbers and shuffling arrays in constant time

    - Track last index
    - Choose a random index
    - Swap the random index with the last index
    - Decrement the last index
    - Repeat again till last index is 0
    """
    def __init__(self, n) -> "RandomGenerator":
        self.remaining = n
        self.arr = [x for x in range(n)]
        self.swaps = {x: x for x in range(n)}

    def generate(self) -> None:
        if self.remaining == 0:
            print("No numbers left to generate")
            return 
        
        last_index = self.remaining - 1
        idx = random.randint(0, last_index)

        # Pick the index
        pick = self.swaps[idx]
        
        # Path compression: replace the picked number with the last index
        self.swaps[idx] = self.swaps[last_index]
        self.remaining -= 1
        print(pick)
        

    def shuffle(self) -> None:
        last_index = len(self.arr) - 1
        while last_index > 0:
            random_index = random.randint(0, last_index)
            self.arr[random_index], self.arr[last_index] = self.arr[last_index], self.arr[random_index]
            last_index -= 1
        
        print(self.arr)


random_machine = FisherYatesRandom(5)
print(random_machine.arr)
random_machine.shuffle()
random_machine.generate()
random_machine.generate()
random_machine.generate()
random_machine.generate()
random_machine.generate()
random_machine.generate()