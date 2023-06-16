import requests

resp = requests.post("https://realtrashline-w5bu4l3kga-et.a.run.app/predict",
                     files={'file': open('test.jpg', 'rb')})

print(resp.json())