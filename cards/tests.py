from django.test import TestCase
import requests

# Create your tests here.



url = f"https://api.scryfall.com/cards/named/" 

params = {"exact": "Black Dragon"}  # Replace with the card name you want

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  # Print the full card data
    print(f"Card Name: {data['name']}")
    print(f"Card_id: {data['collector_number']}")
    print(f"Mana Cost: {data['mana_cost']}")
    print(f"Type Line: {data['type_line']}")
    print(f"Oracle Text: {data['oracle_text']}")
else:
    print(f"Error: {response.status_code}")



