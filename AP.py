import requests
api_key="8b66a510658c972be58a9ee2f59bce3b"
cityName=input("Enter cityName")
weatherData=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=8b66a510658c972be58a9ee2f59bce3b&units=metric".format(cityName))
temp=weatherData.json()
temperature=temp["main"]["temp"]
print("The temperature of city:",cityName,"is",temperature)
