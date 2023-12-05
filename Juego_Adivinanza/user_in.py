
def user_in():
    try:
        user_option = int(input("Introduce la accion deseada: "))
    except ValueError:
        print("Solo puedes introducir numeros")
        
    return user_option    