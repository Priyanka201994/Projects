import requests
api_key="8b66a510658c972be58a9ee2f59bce3b"
cityName=input("Enter cityName:")
weatherData=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=8b66a510658c972be58a9ee2f59bce3b&units=metric".format(cityName))
print(weatherData.status_code)
if(weatherData.status_code==404):
    print("Enter A valid city Name");
else:
    temp=weatherData.json()
    temperature=temp["main"]["temp"]
    print("The temperature of city:",cityName,"is",temperature,"degree celsius")

