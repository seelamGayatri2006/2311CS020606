# Function to get a positive integer from the user
def get_positive_integer():
    while True:
        try:
            n = int(input("Please enter a positive integer: "))
            if n > 0:
                return n
            else:
                print("The number must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
# Main program
def main():
    n = get_positive_integer()

    # Task 2: Print all numbers from 1 to n using a for loop
    print("\nNumbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i)


    # Task 3: Calculate the sum of all numbers from 1 to n using a while loop
    sum_of_numbers = 0
    current_number = 1

    while current_number <= n:
        sum_of_numbers += current_number
        current_number += 1

    print("\nThe sum of all numbers from 1 to", n, "is:", sum_of_numbers)

# Run the main program
if __name__ == "__main__":
    main()







    