n = int(input("Enter a positive integer n: "))
even_sum = 0
for i in range(2, n + 1, 2):  
    even_sum += i
    print(f"The sum of all even numbers between 1 and {n} is: {even_sum}")