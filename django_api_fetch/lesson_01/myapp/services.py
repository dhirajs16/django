import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data['products']
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        return None

