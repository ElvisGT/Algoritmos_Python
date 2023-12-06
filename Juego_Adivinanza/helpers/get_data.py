from json import load
import os

def get_data():
    folder_path = os.path.join("storage")
    file_path = os.path.join(folder_path,"data.json")
    
    print("\nTabla de puntuaciones")
    print("Presiona 4 para volver o 3 para salir")
    
    with open(file_path,"r") as f:
        table_data = load(f)
        
    #Ordenar por los intentos
    table_data.sort(key= lambda attempts: attempts["attempts"])
        
    for data in table_data:
        print("-------------------------")
        print(f"Nombre: {data["name"]} \nIntentos: {data["attempts"]}")
    
    print("-------------------------")
    
    