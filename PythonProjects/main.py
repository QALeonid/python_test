import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6068380bab0094514f10c868cf5b4359'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}


body_registration = {

    "trainer_token": TOKEN,
    "email": "TheHonzikGames@yandex.ru",
    "password": "Vbnm56789"
}
body_confimechen = {
    "trainer_token": TOKEN
}
body_crient = {
    "name": "Бульбазавр4435345",
    "photo_id": 1
}
body_rename = {
    "pokemon_id": "70146",
    "name": "POPOPO123",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "70146"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER,  json = body_registration)
 print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confimechen)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_crient)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''izmenenia = requests.get(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)

message = izmenenia.json()

print(izmenenia)
'''

response_add_poimat = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add_poimat.text)