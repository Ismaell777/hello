import requests

url = 'https://nbu.uz/uz/exchange-rates/json/'

r = requests.get(url)

data = r.json()

print(data)


# 1. List all currencies
# 2. Convert from ...
# 3. Convert to ...

def list_data(currencies):
    for i in currencies:
        created_at = i['date'].split()[0]
        print(i['title'], i['code'], i['cb_price'], created_at)


def list_exchange(exchange):
    a = input('enter a: ')
    for i in exchange:
        if i['code'] == a:
            b = int(input('enter a numb er to convert: '))
            print(
                f"{i['code']} price  is  to UZB value {i['cb_price']}  {float(i['cb_price'])} to {i['code']}")


def list_convert(exchange):
    a = input('enter currency type :')
    for i in exchange:
        if i['code'] == a:
            b = float(input("enter  a number to convert UZD: "))
            print(
                f"{i['code']} price  is to UZB value {i['cb_price']} {b / float(i['cb_price'])} to {i['code']}")


while True:
    print('1. List all currencies')
    print('2. Convert from ...')
    print('3. Convert to ...')

    choice = int(input('Choose an option: '))

    if choice == 1:
        list_data(data)
    elif choice == 2:
        list_exchange(data)
    if choice == 3:
        list_convert(data)
# ____________________________________________________________________________

# import requests

# r = requests.get('https://5f7445deb63868001616029f.mockapi.io/api/words')
#
# data = r.json()
#
# for i in data:
#     # if i['filetype'] == 'audio' or i['filetype'] == 'video':
#     if i['filetype'] in ('audio', 'video'):
#         if 0 < int(i['address'].split('.')[0]) < 100:
#             print(i['name'], i['address'], i['filetype'])
# # _________________________________________________________________________________
# import requests
#
# url = 'https://5f7445deb63868001616029f.mockapi.io/api/words'
#
# r = requests.get(url)
#
#
# data2 = r.json()
#
# for i in data2:
#     if i['filetype'] in ('audio', 'video'):
#         if 0 < int(i['address'].split('.')[0]) < 100:
#             print(i['name'], i['address'], i['filetype'])
#
#

#


