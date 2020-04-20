import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



curr_arr = ("AED","ARS","AUD","BGN","BRL","BSD","CAD","CHF","CLP","CNY","COP","CZK","DKK","DOP","EGP","EUR","FJD","GBP","GTQ","HKD","HRK","IDR","ILS","INR","ISK","JPY","KRW","KZT","MXN","MYR","NOK","NZD","PAB","PEN","PHP","PKR","PLN","PYG","RON","RUB","SAR","SEK","SGD","THB","TRY","TWD","UAH","UAH","USD","UYU","ZAR")

API_KEY = '513ce6b969d531a1b2843dba'


while True:
        action = input("What should I do?\n"
                       "[A]:change current currency\n"
                       "[B]:change new currency\n"
                       "[C]:change amount\n").upper()
        if action not in "ABC" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            currency = input('Please select the currency you have ').upper()
            if currency not in curr_arr:
             print('Currency not supported')
            else:
             response = requests.get("https://prime.exchangerate-api.com/v5/" + API_KEY + "/latest/" + currency)
             new_currency = input('Please select the currency you need ').upper()
             transfer_rate = response.json()['conversion_rates'][new_currency]
             print('Transfer Rate is '+str(transfer_rate)+'\n')
        elif action == 'B':
            new_currency = input('Please select the currency you need ').upper()
            if new_currency not in curr_arr:
             print('Currency not supported')
            else:
             transfer_rate = response.json()['conversion_rates'][new_currency]
             print("Transfer Rate is " + str(transfer_rate) + '\n')
        elif action == 'C':
            amount = input('Enter amount: \n')
            new_amount = float(amount) * transfer_rate
            new_amount=round(new_amount, 2)
            print("Your new amount will be: " + str(new_amount)+'\n')



