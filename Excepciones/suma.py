
sumar = lambda num1,num2 : num1 + num2

while True:
    try:
        num1 = int(input("Teclee un numero: "))
        num2 = int(input("Teclee otro numero: "))
    except ValueError:
        print("El valor tiene que ser numerico")
    else:
        result = sumar(num1,num2)
        print(f"El resultado de la suma de {num1} + {num2} es {result}")
        break