import requests
#getting weather for killeen texas

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 31.1171,
    "longitude": -97.7278,
    'start_date': '2025-12-10',
    'end_date': '2026-01-02',
    'daily': 'temperature_2m_max,temperature_2m_min',
    'temperature_unit': "fahrenheit",
    'timezone': 'America/Chicago' 
}

print('getting weather data...')

response = requests.get(url, params=params)
data = response.json()


if response.status_code != 200:
    print(f"error: {response.status_code}")
    print(response.text)
    exit()




#get the temperature list

dates = data['daily']['time']
highs = data['daily']['temperature_2m_max']
lows =  data['daily']['temperature_2m_min']

#shows the data
print('\nweather for x ~ y')
for i in range(len(dates)):
    print(f'{dates[i]}: High {highs[i]}F,Low {lows[i]}F')

#simple analysis
avg_high = sum(highs) / len(highs)
avg_low = sum(lows) / len(lows)


print(f'\nAvg high: {avg_high}F')
print(f'AVG low: {avg_low}F')
print(f'Hottest day: {max(highs):.1f}f')
print(f'Coldst day:   {min(lows):.1f}F')