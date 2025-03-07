def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a  # Swap işlemi
    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    swap_numbers(a, b)
