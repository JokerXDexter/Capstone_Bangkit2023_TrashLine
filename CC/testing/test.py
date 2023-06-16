import requests

resp = requests.post("https://trashlinefixv2-w5bu4l3kga-et.a.run.app/predict",
                     files={'file': open('test3.jpg', 'rb')})

print(resp.json())