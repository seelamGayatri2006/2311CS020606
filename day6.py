# Function to calculate the square of a number
def calculate_square(n):
    return n * n

# Main program
def main():
    while True:
        try:
            # Ask the user to input a positive integer
            user_input = int(input("Please enter a positive integer: "))
            if user_input > 0:
                break
            else:
                print("The number must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Call the calculate_square function and display the result
    result = calculate_square(user_input)
    print(f"The square of {user_input} is: {result}")

# Run the main program
if __name__ == "__main__":
    main()