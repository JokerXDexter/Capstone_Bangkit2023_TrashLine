import requests

resp = requests.post("https://nutryscan-rvpj3e3pka-uc.a.run.app/predict",
                     files={'file': open('a.jpg', 'rb')})

print(resp.json())