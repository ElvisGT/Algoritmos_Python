from menu import Menu
from user_in import user_in
import os

def main():
    #Mostrar menu
    menu = Menu(["Jugar","Tabla de puntuaciones","Salir"])
    menu.show_menu()
    
    #Opcion de usuario
    option = user_in()
    
    while True:
        if option < 0 or option > 3:
            print("Opcion no valida")
            menu.show_menu()
            option = user_in()
        elif option == 3:
            print("Saliendo...")
            os._exit(0)
            
        elif option == 1:
            print("Jungando")
            break
        
        elif option == 2:
            print("Tabla de puntuaciones")
            break
            

if __name__ == "__main__":
    main()