import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                  "name": "generate",
                   "photo": "generate"
                   },
               headers={
                   'Content-Type': 'application/json', 
                  'trainer_token':'85fe0c5e4dc5e06435871f65fa4e2a8a'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                   "pokemon_id": "19435",
                  "name": "new_Python_name",
                   "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                    },
               headers={
                   'Content-Type': 'application/json', 
                   'trainer_token':'85fe0c5e4dc5e06435871f65fa4e2a8a'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json=
              {"pokemon_id": "19435"},
               headers={
                  'Content-Type': 'application/json', 
                   'trainer_token':'85fe0c5e4dc5e06435871f65fa4e2a8a'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')