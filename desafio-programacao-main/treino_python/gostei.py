import requests

aiai= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")



resultado= aiai.json()
print(resultado['USDBRL']['bid'])