"""
Operator        Name                Syntax
&           Bitwise AND             x & y
|           Bitwise OR              x | y
~           Bitwise NOT             ~x
^           Bitwise XOR             x^y
>>          Bitwise right shift     x>>
<<          Bitwise left shift      x<<

1. AND
- Takes two equal length bit patterns as parameters and performs AND position-wise
e.g. X = 7(111) and Y = 4(100): X & Y = (100) = 4

2. OR
- idem

3. XOR
- idem

4. NOT
- The universal formula is ~x = -(x + 1)
- also we always work with all 8 bits not just the significant ones
e.g. think of 4 as 0000 0100 as opposed to just 100

- Conversion: positive to negative
step 1: convert all bits with ~
    - now we have -(x + 1)
step 2: add 1 in binary

e.g. 10 = 0000 1010
- negate: 1111 0101: this is -1
- add 1: 1111 0110

- Similarly, it's vice versa when we have a negative and wanna read it as a positive: - flip the bits and add one

5. Bitwise Right shift
- shifts the bits to the right
- fill 0 on voids on the left (1 in case of a negative number)
- similar effect as dividing by 2

6. Bitwise Left shift
- shifts bits to the left
- fills 0 on the voids
- similar to multiplying a number by 2

"""
a = 4 # 100
b = 7 # 111

print(f"Bitwise AND: {a} & {b} = ", a & b)
print(f"Bitwise OR: {a} | {b} = ", a | b)
print(f"Bitwise XOR: {a} ^ {b} = ", a ^ b)
print(f"Bitwise NOT: ~{a} = ", ~a)

a = 10 # 0000 1010
b = -10 # 1111 0110
print(f"Right shift: {a} >> 1", a >> 1)
print(f"Right shift: {b} >> 1", b >> 1)


a = 5 # 0000 0101
# a << 1 = 000 01010 # 10
# a << 2 = 0001 0100 # 20

b = -10 # 1111 0110
# Make the BitwiseOperation class. Use method overloading: __and__, __or__, etc. are the builtin names
# Use Pydantic instead of too many if isinstance 

# Checking if a number is odd or even using bitwise operations

# Converting from positive to negative using bitwise operations

# Converting from negative to positive using bitwise operations


"""
1. Converting to binary using bitwise operations
- This is usually done by dividing by 2 until the number becomes zero 
- Dividing by 2 in binary is right shifting: i.e. x = x >> 1
- For negative numbers we use the Two's Complement.

"""
