numbers = [0, 2, 4, 6, 5, 4, 31, 11, 15]

numbers2 = [5, 7, 9, 1]

print(numbers + numbers2)
print(numbers[2])
print(numbers2[1:])

mix = [0, 1, 2, [0, 2, 4]]
print(mix[3][1])

mix.append(100)
print(mix)
mix.remove(100)
print(mix)
del(mix[3])
print(mix)

def checkNumber(number):
    if number % 2 == 0:
        return " é Par"

    return " é Impar"

for number in numbers:
    print(str(number) + checkNumber(number))