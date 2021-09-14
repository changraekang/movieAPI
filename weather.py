from bs4 import BeautifulSoup
import requests

url = "https://weather.com/ko-KR/weather/today/l/KSXX0037:1:KS?Goto=Redirected"

response = requests.get(url)

html_doc = response.text

#print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup)
temperature = soup.select_one("#MainContent .CurrentConditions--tempValue--3a50n")

temp = temperature.text