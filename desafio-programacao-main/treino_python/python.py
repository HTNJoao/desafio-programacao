import json

carros_json= '{"marca": "honda", "modelo": "HRV", "cor": "prata"}'

carros=json.loads(carros_json)

for k,v in carros.items():
    print(k + " == "+ v)