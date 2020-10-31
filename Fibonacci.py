def fibonacci(n):
    if 0 <= n <= 1:
        return n


    a, b = 1, 0

    result = None

    for f in range(n - 1):
        result = b + a
        b = a
        a = result

    return result


fibo = int(input("Enter the number to generate fibonacci series:"))
if fibo <= 0:
    print("Please enter greater number")
for i in range(fibo):
    print(i, fibonacci(i))
