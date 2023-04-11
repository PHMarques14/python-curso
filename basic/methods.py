from str import TXT_NUMERIC_VAL, TXT_ZERO_DIVISION
from str import TXT_INVALID_OPERATION, TXT_KEEP, TXT_OPERATION, TXT_VALUE1, TXT_VALUE2, SOMAR, SUBTRAIR, MULTIPLICAR, DIVIDIR

def sum(val1, val2):
    if not (val1.isnumeric):
        return TXT_NUMERIC_VAL
    if not (val2.isnumeric):
        return TXT_NUMERIC_VAL
    
    result = float(val1) + float(val2)
    return str(result)

def multiply(val1, val2):
    if not (val1.isnumeric):
        return TXT_NUMERIC_VAL
    if not (val2.isnumeric):
        return TXT_NUMERIC_VAL
    result = float(val1) * float(val2)
    return str(result)

def subtract(val1, val2):
    if not (val1.isnumeric):
        return TXT_NUMERIC_VAL
    if not (val2.isnumeric):
        return TXT_NUMERIC_VAL
    result = float(val1) - float(val2)
    return str(result)

def divide(val1, val2):
    if not (val1.isnumeric):
        return TXT_NUMERIC_VAL
    if not (val2.isnumeric):
        return TXT_NUMERIC_VAL
    if (val1 == "0" or val2 == "0"):
        return TXT_ZERO_DIVISION
     
    result = float(val1) // float(val2)
    return str(result)

def identify_operation(operation, val1,val2):
    if operation == SOMAR:
        return sum(val1,val2)
    if operation == SUBTRAIR:
        return subtract(val1,val2)
    if operation == MULTIPLICAR:
        return multiply(val1,val2)
    if operation == DIVIDIR:
        return divide(val1,val2)
    return TXT_INVALID_OPERATION
    
def calc():
    operation = input(TXT_OPERATION)
    val1 = input(TXT_VALUE1)
    val2 = input(TXT_VALUE2)
    result = identify_operation(operation,val1,val2)
    print(result)
    keep = input(TXT_KEEP)
    if keep == "S":
        calc()
    