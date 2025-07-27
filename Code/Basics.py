'''
print("Hello, World!", "This is a basic Python script.")
num = int(input("what is your input?..."))
print(f"You pressed: {num}")

def exponent(x, n):
    # Calculate x raised to the power of n
    return x ** n

exp = exponent(num, 2)
print(f"{num} raised to the power of 2 is: {exp}")
print("Goodbye!")
'''
# List comprehension (creates a list in memory immediately)
squares_list = [x * x for x in range(5)]
print(f"Squares list: {squares_list}")
print(f"Type of squares_list: {type(squares_list)}")
print(f"Size of squares_list (approx): {squares_list.__sizeof__() + sum(x.__sizeof__() for x in squares_list)} bytes")