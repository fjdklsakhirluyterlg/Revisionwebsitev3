import requests

URL = "https://discord.com/api/webhooks/1051545491227299910/DHacX3fNuTkNwypJWU9vnfpSlUztwc-F9Pky-3W21sRDsKOrYHmvmxt5TKp6p5B8otS2"

data = {
    "content" : "",
    "username" : "revisionwebsite"
}

data["embeds"] = [
    {
        "description" : "text in embed",
        "title" : "embed title"
    }
]

def main():
    result = requests.post(URL, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

class discord_notifier:
    def __init__(self, url, name):
        self.url = url
        self.name = name
    
    def add_event():
        dict = {}

if __name__ == "__main__":
    main()