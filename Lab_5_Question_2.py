def multiply(number):
    if number == 1:
        return 3
    else:
        return 3 + multiply(number - 1)


print(multiply(10))