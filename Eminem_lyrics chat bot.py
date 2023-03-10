import requests
import json

a=['godzilla','speedom','venom','Hello','rap god','The Real Slim Shady','go to sleep']
b=list(map(lambda s:s+'\n\n'+json.loads(requests.get('https://api.music.msub.kr/?song=eminem%20'+s).text)['song'][0]['lyrics'], a))

print('\n--------------------------\n\n'.join(b))
#print(json.loads(requests.get('http://api.music.msub.kr/?song=eminem').text)['song'][0]['lyrics'])

