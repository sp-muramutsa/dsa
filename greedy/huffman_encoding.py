from collections import Counter, deque
from math import ceil, log2
import heapq


class FixedLength:
    def encode(self, text):
        """
        Input: 
            - text: str. The text to be encoded
        
        Output:
            - result: list. The encoded text.
            - new_map: dict. the dictionary of the new codes

        TODO:   Actually packing the encoded strings into bytes. 
                Note that we're still treating them as pythnon strings which can be large.

        """
        frequency = Counter(text)
        n = len(frequency)
        new_codes = self._generate_binary_codes_(list(frequency.keys()))

        encoded_text = []
        for char in text:
            encoded_text.append(new_codes[char])

        new_codes = {v: k for k, v in new_codes.items()}
        return (encoded_text, new_codes)

    def decode(self, encoded_text: list, new_codes: dict):
        decoded_text = [new_codes[char] for char in encoded_text]
        return "".join(decoded_text)

    def _generate_binary_codes_(self, chars: list):
        """
        Generates the binary numbers from 0 to n
        """

        n = len(chars)
        if n > 1:
            bit_length = ceil(log2(n))
        else:
            bit_length = n

        unique_codes = {}
        for i, char in enumerate(chars):
            unique_codes[char] = f"{i:0{bit_length}b}"
        
        return unique_codes        

class Node:
    def __init__(self, char="", freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"char: {self.char}, freq: {self.freq}"
    
    def __lt__(self, other):
        return self.freq < other.freq

class VariableLength:
    def __init__(self):
        self.heap = []
        self.codes_to_chars = {}
        self.chars_to_codes = {}

    def encode(self, text):
        """
        Huffman Encoding. Create a Huffman tree.
        """

        # Get frequency
        frequency = Counter(text)
        n = len(frequency)

        # Sort in increasing order of frequency
        for char, count in frequency.items():
            heapq.heappush(self.heap, Node(char, count))

        # Construct the tree
        for i in range(n - 1):
            new_node = Node()
            left_node = heapq.heappop(self.heap)
            right_node = heapq.heappop(self.heap)

            new_node.left = left_node
            new_node.right = right_node
            new_node.freq = left_node.freq + right_node.freq
            heapq.heappush(self.heap, new_node)
        
        # Get the codes
        self.pre_order(self.heap[0], "")
        
        # Encode the text
        encoded_text = [self.chars_to_codes[char] for char in text]
        print(text)
        print(encoded_text)
        print(self.codes_to_chars)

    def decode(self, text):
        """
        TODO: should be fairly trivial
        """
        pass
        
    
    def pre_order(self, root, curr):
        if not root:
            return
        
        # Root leaf
        if root.left is None and root.right is None:
            # Single character case
            if curr == "":
                curr = "0"
            self.codes_to_chars[curr] = root.char
            self.chars_to_codes[root.char] = curr
            return
        
        self.pre_order(root.left, curr + '0')
        self.pre_order(root.right,  curr + '1')

        

def main():
    test_text = "BCCABBDDAECCBBAEDDCC"
    # fl = FixedLength()
    # encoded_text, new_codes = fl.encode("Hello world")
    # print(encoded_text, new_codes)
    # decoded_text = fl.decode(encoded_text, new_codes)
    # print(decoded_text)

    vl = VariableLength()
    vl.encode(test_text)
    vl.decode(test_text)

if __name__ == "__main__":
    main()