print("Hello, World!", "This is a basic Python script.")
num = int(input("Press Enter to exit..."))
print(f"You pressed: {num}")

def exponent(x, n):
    # Calculate x raised to the power of n
    return x ** n

exp = exponent(num, 2)
print(f"{num} raised to the power of 2 is: {exp}")
print("Goodbye!")

