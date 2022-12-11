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
    def __init__(self, url, content="", embeds:list=[]):
        self.url = url
        self.userame = "revisionwebsite"
        self.content = content
        self.embeds = embeds
    
    def dict_event(self):
        dict = {}
        dict["username"] = self.userame
        dict["url"] = self.url
        dict["embeds"] = self.embeds

        return dict
    
    def add_embed(self, event:dict):
        self.embeds.append(event)
    
    def send(self):
        data = self.dict_event()
        result = requests.post(URL, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            return result.status_code

if __name__ == "__main__":
    new = discord_notifier(url="https://discord.com/api/webhooks/1051545491227299910/DHacX3fNuTkNwypJWU9vnfpSlUztwc-F9Pky-3W21sRDsKOrYHmvmxt5TKp6p5B8otS2", embeds=[{"description" : "text in embed","title" : "embed title", "color":0xFF5733}])
    res = new.send()
    print(res)
