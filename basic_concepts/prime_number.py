

def is_prime_number(number):

    is_prime = True
    if number < 2:
        is_prime = False

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    return is_prime


input_range = input("Enter the range: ").split()

minimum = int(input_range[0])
maximum = int(input_range[1])

# print(f"List of prime number between {minimum} and {maximum} : ")

list = []
for i in range(minimum, maximum):
    if is_prime_number(i):
        list.append(i)
print(f"List of prime numbers between {minimum} and {maximum}:  {list}")
