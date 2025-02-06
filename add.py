# Function to compute the sum of two numbers
def sum_two_numbers():
    # Read input: two space-separated integers
    a, b = map(int, input("Enter two space-separated numbers: ").split())
    # Calculate the sum
    result = a + b
    # Print the result
    print("The sum is:", result)

# Call the function
sum_two_numbers()