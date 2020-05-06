superMarket = {
    'storeA': {
        'name': 'A store',
        'items': [
            {'name': 'A01', 'quantity': 10},
            {'name': 'A02', 'quantity': 100},
            {'name': 'A03', 'quantity': 100}
        ]
    },
    'storeB': {
        'name': 'B store',
        'items': [
            {'name': 'B01', 'quantity': 1000},
            {'name': 'B02', 'quantity': 100},
            {'name': 'B03', 'quantity': 10}
        ]
    }
}

print(superMarket)

print()

print('Store A -> Type ->', type(superMarket['storeA']),
      " value -> superMarket['storeA'] -> ", superMarket['storeA'])
print('Name of store-1 ->', "superMarket.get('storeA').get('name') ->", superMarket.get('storeA').get('name'))
print('Name of store-1 ->', "superMarket['storeA']['name'] ->", superMarket.get('storeA').get('name'))

print()

print('All item names present in store 1 ->')
for item in superMarket['storeA']['items']:
    print(item['name'])

print()

for item in superMarket['storeB']['items']:
    if item['name'] == 'B02':
        print('Quantity of {} in {} is -> {}'
              .format(item['name'], superMarket['storeB']['name'], item['quantity']))

# {'storeA': {'name': 'A store', 'items': [{'name': 'A01', 'quantity': 10}, {'name': 'A02', 'quantity': 100}, {'name': 'A03', 'quantity': 100}]}, 'storeB': {'name': 'B store', 'items': [{'name': 'B01', 'quantity': 1000}, {'name': 'B02', 'quantity': 100}, {'name': 'B03', 'quantity': 10}]}}
#
# Store A -> Type -> <class 'dict'>  value -> superMarket['storeA'] ->  {'name': 'A store', 'items': [{'name': 'A01', 'quantity': 10}, {'name': 'A02', 'quantity': 100}, {'name': 'A03', 'quantity': 100}]}
# Name of store-1 -> superMarket.get('storeA').get('name') -> A store
# Name of store-1 -> superMarket['storeA']['name'] -> A store
#
# All item names present in store 1 ->
# A01
# A02
# A03
#
# Quantity of B02 in B store is -> 100
