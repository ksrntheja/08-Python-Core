import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print('type(response)', type(response))
binfo = response.json()  # provides python's dict object
print('type(binfo)', type(binfo))
print(binfo)
print()
print('Bitcoin Price as on', binfo['time']['updated'])
print('1 BitCoin = $', binfo['bpi']['USD']['rate'])

# type(response) <class 'requests.models.Response'>
# type(binfo) <class 'dict'>
# {
#   'time':
#           {
#               'updated': 'May 25, 2020 08:18:00 UTC',
#               'updatedISO': '2020-05-25T08:18:00+00:00',
#               'updateduk': 'May 25, 2020 at 09:18 BST'
#           },
#   'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org',
#   'chartName': 'Bitcoin',
#   'bpi':
#       {
#           'USD': {
#                       'code': 'USD',
#                       'symbol': '&#36;',
#                       'rate': '8,825.2807',
#                       'description': 'United States Dollar',
#                       'rate_float': 8825.2807
#                  },
#           'GBP': {
#                       'code': 'GBP',
#                       'symbol': '&pound;',
#                       'rate': '7,254.0542',
#                       'description': 'British Pound Sterling',
#                       'rate_float': 7254.0542
#                   },
#           'EUR': {
#                       'code': 'EUR',
#                       'symbol': '&euro;',
#                       'rate': '8,114.5102',
#                       'description': 'Euro', 'rate_float': 8114.5102
#                   }
#       }
# }
#
# Bitcoin Price as on May 25, 2020 08:18:00 UTC
# 1 BitCoin = $ 8,825.2807
