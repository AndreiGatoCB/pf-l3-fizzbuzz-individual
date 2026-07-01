mil = 1000
for numero in range(mil):
    numero += 1
    if numero % 3 == 0:
        if numero % 5 == 0:
            print("Fizzbuzz")
        else:
            print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
