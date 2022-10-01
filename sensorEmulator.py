import requests
import random


def sendData():
    params = {
        "pressure": random.randrange(1006, 1012),
        "temperature": random.randrange(-12, 36),
        "light": random.randrange(100, 500),
    }
    print(params)

    req = requests.post(
        "https://us-central1-iot-lpdim.cloudfunctions.net/insert",
        json=params,
        headers={"Content-Type": "application/json"},
    )

    print(req.text)


sendData()
