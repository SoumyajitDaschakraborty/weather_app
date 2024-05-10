import requests

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=7a7f9d7067854757b85135818242701&q={city}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
