def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2    

def div(num1, num2):
    return num1 / num2    

def pow(num1, num2):
    return num1 ** num2    


sum = sum(2,2)
sub = sub(5,4)
multi = multi(2,10)
div = div(40,2)
pow = pow(2,3)

result = sum + sub + multi - div + pow
print(result >= 0 and "Greater than zero" or "Sub-zero!")


name = "Gustavo"
last_name = "Ramos"

print(name + " " + last_name)