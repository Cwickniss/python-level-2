import requests
from bs4 import BeautifulSoup

GET_DATA = True

URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

name = None
email = None

headers = {'User-Agent': f'{name} ({email})'}

if GET_DATA:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    html_doc = response.text
    with open('countries.html', 'w', encoding="utf-8") as file:
        file.write(html_doc)
else:
    with open('countries.html', 'r', encoding="utf-8") as file:
        html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find('table', class_='wikitable')

countries = []

rows = table.find_all('tr')
for row in rows:
    name_col = row.th
    link = name_col.a
    if link is None:
        continue
    name = link.string
    countries.append(name)

print(countries)
print(len(countries))

with open('countries.txt', 'w') as file:
    for country in countries:
        file.write(country + '\n')
