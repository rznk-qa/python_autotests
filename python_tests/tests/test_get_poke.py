import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 3348})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 3348})
    trainer_name = response.json()['trainer_name']
    assert trainer_name == 'rznk'

def test_city():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 3348})
    city = response.json()['city']
    assert city == 'NN'

def test_status_code_debug():
    response = requests.get(url=f'{HOST}/debug_sentry')
    assert response.status_code == 500
