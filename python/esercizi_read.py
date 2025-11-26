import json
def read_config(path):
    try:
        with open(path) as file:
            data = json.loads(file.read())
            print(data["threshold"])
    except:
        print("Errore riscontrato")
        
read_config("config.json")

def user_info(path):
    with open(path) as file:
        user = json.loads(file.read())
        return f"{user["name"]} ha {user["age"]} e conosce {", ".join(user["skills"])}"
    
print(user_info("user.json"))

def get_specs(path):
    try:
        with open(path) as file:
            data = json.load(file)
            specs = data["product"]["specs"]
            result = ", ".join(f"{key}: {value}"for key, value in specs.items())
            return result
    except FileNotFoundError:
        print(" File non trovato")


print(get_specs("product.json"))

def change_sett(path):
    #manca try
    with open(path) as file:
        data = json.load(file)
    data["sound"] = False
    with open(path,"w") as file:
        #file.write(json.dumps(data))
        json.dump(data,file, indent=4) #formato json typesh
    

change_sett("settings.json")

def errors(path):
    count = 0
    data = {}
    with open(path) as file:
        for line in file:
            key,value = line.split(":")
            data[key] = data.get(key,[])
            data[key].append(value)
            
        print(data)
print(f"Errori totali {errors('log.txt')}")
