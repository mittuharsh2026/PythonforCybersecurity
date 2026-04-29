
def is_divisible(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False


number = int(input("What is the number: "))
divisor = int(input("What is the divisor: "))


if is_divisible(number, divisor):
    print(f"{number} is divisible by {divisor}")
else:
    print(f"{number} is NOT divisible by {divisor}")
