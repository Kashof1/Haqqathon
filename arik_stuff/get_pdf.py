import requests

url = 'https://ec.europa.eu/eurostat/documents/1978984/6037342/ISCO-08.pdf'
response = requests.get(url)

with open('ISCO-08.pdf', 'wb') as file:
    file.write(response.content)