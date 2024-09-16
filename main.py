import requests
import json

def getData():

    productos={
        "title":"Laptops",
        "description":"Your perfect pack for everyday use and walks in the forest",
        "price":"109.95",
        "image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        "category":"men's clothing"
    }
    
    try:
        #response= requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
        response=requests.post('https://fakestoreapi.com/products',productos)
        
        
        print(json.dumps(response.json(),indent=2) )
    except requests.exceptions.RequestException as er:
        print(f"Eerror al consumir la API : {er}")
        
if __name__=="__main__":
    getData()

