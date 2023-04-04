def sum(val1, val2):
    result = float(val1) + float(val2)
    return str(result)

def multiply(val1, val2):
    result = float(val1) * float(val2)
    return str(result)

def subtract(val1, val2):
    result = float(val1) - float(val2)
    return str(result)

def divide(val1, val2):
    result = float(val1) // float(val2)
    return str(result)


value_1 = input("Digite o valor 1: ")
value_2 = input("Digite o valor 2: ")

#result = sum(value_1,value_2)
result = multiply(value_1,value_2)
#result = subtract(value_1,value_2)
#result = divide(value_1,value_2)

print(result)
