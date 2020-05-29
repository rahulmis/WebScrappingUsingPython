import requests
import shutil
url = 'https://img.pokemondb.net/artwork/large/weedle.jpg'
im = requests.get(url,stream=True)
path = open('pokemon1.ico','wb')
shutil.copyfileobj(im.raw,path)