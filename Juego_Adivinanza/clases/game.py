from random import randrange

class Game:
    def __init__(self):
        self.num_random = randrange(0,100)
        self.attempts = 0
        self.user_opt = 0
        self.user_name = ""
        
    def play(self):
        self.user_name = input("Ingrese su nombre: ")
        while True:
            try: 
                self.user_opt = int(input("Ingrese el numero: "))
            except ValueError:
                print("Debe ser un valor numerico")
            else:
                if self.user_opt == self.num_random:
                    print(f"Has ganado en {self.attempts} intentos")
                    break
                elif self.user_opt > self.num_random:
                    print("Demasiado alto, prueba mas bajo")
                    self.attempts += 1
                elif self.user_opt < self.num_random:
                    print("Demasiado bajo, prueba mas alto")
                    self.attempts += 1
                
    def get_data(self):
        user_data = {
            "name":self.user_name,
            "attemps": self.attempts
        }
        return user_data
    