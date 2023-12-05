from json import dump,load
import os


def save_data(user_data):
    folder_path = os.path.join("storage")
    file_path = os.path.join(folder_path,"data.json")
    is_name = False
    
    #Verifico si existe
    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            current_data = load(f)
            #verifico si existe el nombre en el registro
            for dicts in current_data:
                for key,value in dicts.items():
                    if value.lower() == user_data["name"].lower():
                        is_name = True
                        print(key)
            #Si el nombre no existe
            if not is_name:
                current_data.append(user_data)
           
    else:
        current_data = [user_data]
    
    with open(file_path,"w") as f:
        dump(current_data,f)
    print("Se ha guardado exitosamente")
    
    
save_data({
    "name":"elvis"
})