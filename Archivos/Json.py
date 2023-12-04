from json import dump,load

class Json:
    def __init__(self,path,data):
        self.path = path
        self.data = data
    
    def save_data(self):
        with open(self.path,"w") as f:
            dump(self.data,f)
    
    def read_data(self):
        with open(self.path,"r") as f:
            return load(f)
        
    
data = {
    "name":"EGT",
    "edad":24
}   
json = Json('./data.json',data)
# json.save_data()

try:
    print(json.read_data())
except FileNotFoundError:
    pass

    