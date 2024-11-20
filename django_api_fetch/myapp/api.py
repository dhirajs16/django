import requests

def fetch():
    response = requests.get("https://fakestoreapi.in/api/products?limit=150")
    data = response.json()
    return data['products']

