from clases.menu import Menu
from clases.game import Game
from helpers.user_in import user_in
from helpers.save_data import save_data
from helpers.get_data import get_data
import os

def main():
    #Mostrar menu
    menu = Menu(["Jugar","Tabla de puntuaciones","Salir"])
    menu.show_menu()
    
    #Opcion de usuario
    option = user_in()
    
    while True:
        if option < 0 or option > 4:
            print("Opcion no valida")
            menu.show_menu()
            option = user_in()
        elif option == 3:
            print("Saliendo...")
            os._exit(0)
            
        elif option == 1:
            #Inicializar Game
            game = Game()
            game.play()
            #guardar en base de datos la puntuacion
            save_data(game.get_data())
            break
        
        elif option == 2:
            get_data()
            option = user_in()
            if option == 4:
                menu.show_menu()
            else:
                print("Saliendo...")
                os._exit(0)
        
        elif option == 4:
            menu.show_menu()
            option = user_in()

if __name__ == "__main__":
    main()