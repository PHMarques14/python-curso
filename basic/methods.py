from str import TXT_NUMERIC_VAL, TXT_ZERO_DIVISION, TXT_NO_NEGATIVES
from str import TXT_INVALID_OPERATION, TXT_OPTION_KEEP, TXT_OPERATION, TXT_VALUE1, TXT_VALUE2, SOMAR, SUBTRAIR, MULTIPLICAR, DIVIDIR, SAIR

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def sum(val1, val2):
    if not is_float(val1):
        return TXT_NUMERIC_VAL
    if not is_float(val2):
        return TXT_NUMERIC_VAL
    
    result = float(val1) + float(val2)
    return result

def multiply(val1, val2):
    if not is_float(val1):
        return TXT_NUMERIC_VAL
    if not is_float(val2):
        return TXT_NUMERIC_VAL
    result = float(val1) * float(val2)
    return result

def subtract(val1, val2):
    if not is_float(val1):
        return TXT_NUMERIC_VAL
    if not is_float(val2):
        return TXT_NUMERIC_VAL
    
    if float(val2) > float(val1):
        return TXT_NO_NEGATIVES
    
    result = float(val1) - float(val2)
    return result

def divide(val1, val2):
    if not is_float(val1):
        return TXT_NUMERIC_VAL
    if not is_float(val2):
        return TXT_NUMERIC_VAL
    if (val1 == "0" or val2 == "0"):
        return TXT_ZERO_DIVISION
     
    result = float(val1) // float(val2)
    return result

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
    if operation == None:
        return
    val1 = input(TXT_VALUE1)
    val2 = input(TXT_VALUE2)
    result = identify_operation(operation,val1,val2)  
    print(result)
    option_keep = input(TXT_OPTION_KEEP)
    if option_keep == "S":
        calc()
    
def advanced_calc():
    val1 = input(TXT_VALUE1)
    
    next_calc(val1)
    
def next_calc(val1):
    
    operation = input(TXT_OPERATION)
    
    if operation == SAIR:
        return
    
    val2 = input(TXT_VALUE2)
    
    result = identify_operation(operation,val1,val2)
    
    if isinstance(result,str):
        print(result)
        new_val_1 = input(TXT_VALUE1)
        next_calc(new_val_1)
    else:
        print(result)
        next_calc(result)    
        return result