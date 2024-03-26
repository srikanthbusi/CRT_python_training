def sum_of_even_numbers(arr):
    # Split the input string into a list of integers
    num = list(map(int, arr.split()))
    
    # Initialize a variable to store the sum of even numbers
    sum_even = 0
    
    # Iterate through the list of numbers
    for i in num:
        # Check if the number is even
        if i % 2 == 0:
            # Add the even number to the sum
            sum_even += i
    
    return sum_even

# Input space-separated integers
input_str = input("Enter space-separated integers: ")

# Call the function and print the result
print("Sum of even numbers:", sum_of_even_numbers(input_str))
