import requests

url = 'http://localhost:5000/get_form'

data1 = {'reg_email': 'john.doe@example.com',
         'date_of_birth': '2002-08-12', 'password': 'secretword'}
response1 = requests.post(url, data=data1)
print("Response 1:", response1.json())

data2 = {'first_name': 'Alice', 'old_date': '2022-01-01',
         'last_name': 'random_text'}
response2 = requests.post(url, data=data2)
print("Response 2:", response2.json())

data3 = {'main_phone': '+71234567890',
         'main_email': 'invalid_email@example.com'}
response3 = requests.post(url, data=data3)
print("Response 3:", response3.json())
