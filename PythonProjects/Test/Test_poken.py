import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6068380bab0094514f10c868cf5b4359'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 7285

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert  response.status_code == 200 

def test_ret_of_response():
    response_get = requests.get(url= f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == '134'