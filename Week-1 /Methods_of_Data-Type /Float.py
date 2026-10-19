# 1. as_integer_ratio

# Q1: WAP to get the integer ratio of a float
f = 0.5
print("Integer Ratio:", f.as_integer_ratio())
# Q2: WAP to get the ratio of a whole float number
f = 2.0
print("Integer Ratio:", f.as_integer_ratio())
# Q3: WAP to get the ratio of a negative float
f = -1.25
print("Integer Ratio:", f.as_integer_ratio())
# Q4: WAP to get the ratio of a standard decimal float
f = 0.75
print("Integer Ratio:", f.as_integer_ratio())

# 2. conjugate

# Q1: WAP to get the complex conjugate of a float
f = 5.5
print("Conjugate:", f.conjugate())
# Q2: WAP to get the conjugate of a negative float
f = -3.2
print("Conjugate:", f.conjugate())
# Q3: WAP to get the conjugate of zero float
f = 0.0
print("Conjugate:", f.conjugate())
# Q4: WAP to verify that a float's conjugate equals itself
f = 12.34
print("Is conjugate equal to float?", f.conjugate() == f)

# 3. fromhex

# Q1: WAP to create a float from a hexadecimal string representation
s = "0x1.0p+0"
print("From Hex:", float.fromhex(s))
# Q2: WAP to create a float from another hex string value
s = "0x1.8p+1"
print("From Hex:", float.fromhex(s))
# Q3: WAP to convert a negative hex string to float
s = "-0x2.0p+0"
print("From Hex:", float.fromhex(s))
# Q4: WAP to convert a fractional hex representation to float
s = "0x0.8p+0"
print("From Hex:", float.fromhex(s))

# 4. hex

# Q1: WAP to convert a float to its hexadecimal string representation
f = 2.0
print("Hex Representation:", f.hex())
# Q2: WAP to get the hex string of a negative float
f = -3.0
print("Hex Representation:", f.hex())
# Q3: WAP to get the hex string of a fractional float
f = 0.5
print("Hex Representation:", f.hex())
# Q4: WAP to check hex representation of zero float
f = 0.0
print("Hex Representation:", f.hex())

# 5. imag

# Q1: WAP to get the imaginary part of a float
f = 4.5
print("Imaginary Part:", f.imag)
# Q2: WAP to get the imaginary part of a negative float
f = -7.8
print("Imaginary Part:", f.imag)
# Q3: WAP to get the imaginary part of zero float
f = 0.0
print("Imaginary Part:", f.imag)
# Q4: WAP to verify that imaginary part is always zero for floats
f = 9.9
print("Is imaginary part zero?", f.imag == 0.0)

# 6. is_integer

# Q1: WAP to check if a whole float value represents an integer
f = 10.0
print("Is integer?", f.is_integer())
# Q2: WAP to check is_integer on a decimal float value
f = 10.5
print("Is integer?", f.is_integer())
# Q3: WAP to check is_integer on zero float
f = 0.0
print("Is integer?", f.is_integer())
# Q4: WAP to check is_integer on a negative decimal float
f = -3.14
print("Is integer?", f.is_integer())

# 7. real

# Q1: WAP to get the real part of a float
f = 6.7
print("Real Part:", f.real)
# Q2: WAP to get the real part of a negative float
f = -4.2
print("Real Part:", f.real)
# Q3: WAP to get the real part of zero float
f = 0.0
print("Real Part:", f.real)
# Q4: WAP to verify real part matches the float value itself
f = 8.12
print("Does real part match float?", f.real == 8.12)
