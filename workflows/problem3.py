def decimal_to_binary(n):
    # List to store the binary digits
    binary_digits = []
    
    # Algorithm to convert decimal to binary
    while n > 0:
        remainder = n % 2
        binary_digits.append(remainder)
        n = n // 2
    
    # The binary equivalent is the sequence of remainders read from bottom to top
    binary_digits.reverse()
    
    # Join the binary digits to form the final binary number string
    binary_str = ''.join(map(str, binary_digits))
    
    return binary_str

def main():
    # Example Inputs
    inputs = [5, 255, 18]
    
    for number in inputs:
        binary_result = decimal_to_binary(number)
        print(f"Input: {number}\nOutput: {binary_result}\n")

if __name__ == "_main_":
    main()