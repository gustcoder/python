#import calc #importa todos os metodos do modulo
from schoolofnet.math.calc import calculate #importa modulos em especifico
from schoolofnet.string.str import concatenate

sum = calculate(10,20)
str = concatenate('A soma ', 'é:')

print(str)
print(sum)