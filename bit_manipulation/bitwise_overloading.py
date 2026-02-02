class Bitwise:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __and__(self, other):
        return Bitwise(self.value & other.value)
    
    def __or__(self, other):
        return Bitwise(self.value | other.value)
    
    def __invert__(self):
        return Bitwise(~self.value)
    
    def __xor__(self, other):
        return Bitwise(self.value ^ other.value)
    
    def __lshift__(self, other):
        return Bitwise(self.value << other.value)
    
    def __rshift__(self, other):
        return Bitwise(self.value >> other.value)

if __name__ == "__main__":
    a = Bitwise(4)
    b = Bitwise(6)
    c = Bitwise(7)

    print(a & b)
    print(a | b)
    print(~a)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print((a & b) | c)