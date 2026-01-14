# projects/webS.py
'''
* Author: TanB
* Created: 8/18/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.codedex.io/intermediate-python/20-caffeinated'
response = requests.get(url)
print(response.text)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wins64; x64)'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())




