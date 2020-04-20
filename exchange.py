import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


API_KEY = '513ce6b969d531a1b2843dba'
currency = input('Please select the currency you have ')

response = requests.get("https://prime.exchangerate-api.com/v5/"+API_KEY+"/latest/"+currency)
new_currency = input('Please select the currency you need ')
transfer_rate = response.json()['conversion_rates'][new_currency]
print('The transfer rate from '+currency+' to '+new_currency+' is '+str(transfer_rate))
amount = input('Enter amount: ')

new_amount = float(amount)*transfer_rate
round(new_amount, 3)
print('Your new amount will be: '+str(new_amount))
print(response.status_code)
#jprint(response.json())
