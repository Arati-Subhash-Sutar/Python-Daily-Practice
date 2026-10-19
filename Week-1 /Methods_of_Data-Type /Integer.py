# bit_count

# Q1: WAP to count the number of set bits in an integer
n = 5
print(n.bit_count())
# Q2: WAP to count the set bits in zero
n = 0
print(n.bit_count())
# Q3: WAP to count the set bits in a larger number
n = 255
print(n.bit_count())
# Q4: WAP to count the set bits in a negative number's absolute representation
n = -5
print(n.bit_count())

# bit_length

# Q1: WAP to find the number of bits needed to represent an integer in binary
n = 4
print(n.bit_length())
# Q2: WAP to find the bit length of a larger number
n = 10
print(n.bit_length())
# Q3: WAP to find the bit length of number one
n = 1
print(n.bit_length())
# Q4: WAP to find the bit length of zero
n = 0
print(n.bit_length())

# conjugate

# Q1: WAP to get the complex conjugate of an integer
n = 5
print(n.conjugate())
# Q2: WAP to get the conjugate of a negative integer
n = -10
print(n.conjugate())
# Q3: WAP to check conjugate of zero
n = 0
print(n.conjugate())
# Q4: WAP to verify that an integer's conjugate is equal to itself
n = 42
print(n.conjugate() == n)

# denominator

# Q1: WAP to get the denominator of an integer
n = 7
print(n.denominator)
# Q2: WAP to get the denominator of a negative integer
n = -15
print(n.denominator)
# Q3: WAP to get the denominator of zero
n = 0
print(n.denominator)
# Q4: WAP to check denominator property value
n = 100
print(n.denominator)

# from_bytes

# Q1: WAP to create an integer from a byte representation in big-endian order
b = b'\x00\x05'
print(int.from_bytes(b, byteorder='big'))
# Q2: WAP to create an integer from bytes in little-endian order
b = b'\x05\x00'
print(int.from_bytes(b, byteorder='little'))
# Q3: WAP to create a signed integer from bytes
b = b'\xff'
print(int.from_bytes(b, byteorder='big', signed=True))
# Q4: WAP to create an integer from a single byte
b = b'\x0a'
print(int.from_bytes(b, byteorder='big'))

# imag

# Q1: WAP to get the imaginary part of an integer
n = 12
print(n.imag)
# Q2: WAP to get the imaginary part of a negative integer
n = -8
print(n.imag)
# Q3: WAP to get the imaginary part of zero
n = 0
print(n.imag)
# Q4: WAP to check if imaginary part is always zero for integers
n = 99
print(n.imag == 0)

# is_integer

# Q1: WAP to check if an integer value is an integer
n = 10
print(n.is_integer())
# Q2: WAP to check integer status on zero
n = 0
print(n.is_integer())
# Q3: WAP to check integer status on a negative integer
n = -5
print(n.is_integer())
# Q4: WAP to verify is_integer on a large whole number
n = 1000
print(n.is_integer())

# numerator

# Q1: WAP to get the numerator of an integer
n = 14
print(n.numerator)
# Q2: WAP to get the numerator of a negative integer
n = -25
print(n.numerator)
# Q3: WAP to get the numerator of zero
n = 0
print(n.numerator)
# Q4: WAP to verify numerator property equals the number itself
n = 50
print(n.numerator == n)

# real

# Q1: WAP to get the real part of an integer
n = 18
print(n.real)
# Q2: WAP to get the real part of a negative integer
n = -3
print(n.real)
# Q3: WAP to get the real part of zero
n = 0
print(n.real)
# Q4: WAP to verify real part matches the integer value
n = 77
print(n.real == 77)

# to_bytes

# Q1: WAP to convert an integer to a 2-byte big-endian representation
n = 5
print(n.to_bytes(2, byteorder='big'))
# Q2: WAP to convert an integer to bytes in little-endian order
n = 5
print(n.to_bytes(2, byteorder='little'))
# Q3: WAP to convert a negative signed integer to bytes
n = -1
print(n.to_bytes(1, byteorder='big', signed=True))
# Q4: WAP to convert a larger integer to a 4-byte format
n = 1024
print(n.to_bytes(4, byteorder='big'))
