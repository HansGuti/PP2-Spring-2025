import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)


print('Interface status')
print('=' * 80)
print(f'{"DN":<50} {"Description":<20} {"Speed":<10} {"MTU":<10}')
print('-' * 80)
    
for i in data['imdata']:
    att = i['l1PhysIf']['attributes']
    dn = att['dn']
    descr = att['descr'] if att['descr'] else ''
    speed = att['speed']
    mtu = att['mtu']

    print(f'{dn:<50} {descr:<20} {speed:<10} {mtu:<10}')

