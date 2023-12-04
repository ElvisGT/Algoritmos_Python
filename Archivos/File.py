class File:
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
        
    def open_file(self):
        with open(self.file_path) as files:
            for file in files:
                print(file)
            files.close()
    def create_file(self):
        with open(self.file_path,"w") as file:
            file.write("Esto es un mensaje de prueba de Java en el archivo creado")
            file.close()
    def replace_word(self,word,new_word):
        with open(self.file_path,"r") as files:
            new_content = files.read().replace(word,new_word)
        
        with open(self.file_path,"w") as file:
            file.write(new_content)
            
            
    
                
file = File("file.txt","./file.txt")

file.create_file()

file.open_file()

file.replace_word("Java","python")

file.open_file()

file.replace_word("python","Elvis")

file.open_file()
