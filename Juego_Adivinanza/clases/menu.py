
class Menu:
    def __init__(self,options):
        self.options = options
        
    def show_menu(self):
        print("\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
        for i,option in enumerate(self.options):
            print(f"{i + 1}: {option}")  
        print("\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")

