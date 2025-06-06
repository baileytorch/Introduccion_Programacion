str_numero = input("Ingrese un número entero")

try:
    if float(str_numero).is_integer():
        print("integer")
    else:
        print("float")
except ValueError:
    print("not integer or float")