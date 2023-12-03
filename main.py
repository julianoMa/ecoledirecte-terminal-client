import requests
from datetime import datetime
import json
from dotenv import load_dotenv
import os

class Login():
    def __init__(self):
        self.get_credentials()

    def get_credentials(self):
        os.system('cls||clear')
        print("""\n\n▓█████  ▄████▄   ▒█████   ██▓    ▓█████    ▓█████▄  ██▓ ██▀███  ▓█████  ▄████▄  ▄▄▄█████▓▓█████     ▄████▄   ██▓     ██▓▓█████  ███▄    █ ▄▄▄█████▓
▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▓█   ▀    ▒██▀ ██▌▓██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓█   ▀    ▒██▀ ▀█  ▓██▒    ▓██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
▒███   ▒▓█    ▄ ▒██░  ██▒▒██░    ▒███      ░██   █▌▒██▒▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒███      ▒▓█    ▄ ▒██░    ▒██▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒▓█  ▄    ░▓█▄   ▌░██░▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓█  ▄    ▒▓▓▄ ▄██▒▒██░    ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
░▒████▒▒ ▓███▀ ░░ ████▓▒░░██████▒░▒████▒   ░▒████▓ ░██░░██▓ ▒██▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░▒████▒   ▒ ▓███▀ ░░██████▒░██░░▒████▒▒██░   ▓██░  ▒██▒ ░ 
░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░░ ▒░ ░    ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
 ░ ░  ░  ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░ ░ ░  ░    ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░ ░ ░  ░  ░  ▒       ░     ░ ░  ░     ░  ▒   ░ ░ ▒  ░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░    ░    
   ░   ░        ░ ░ ░ ▒    ░ ░      ░       ░ ░  ░  ▒ ░  ░░   ░    ░   ░          ░         ░      ░          ░ ░    ▒ ░   ░      ░   ░ ░   ░      
   ░  ░░ ░          ░ ░      ░  ░   ░  ░      ░     ░     ░        ░  ░░ ░                  ░  ░   ░ ░          ░  ░ ░     ░  ░         ░          
       ░                                    ░                          ░                           ░                                               

""")
        self.identifiant = input("\nlogin as : ")
        self.password = input(f"{self.identifiant}'s password : ")

        self.data = {
            "identifiant": self.identifiant,
            "motdepasse": self.password,
            "isReLogin": False,
            "uuid": ""
        }

        self.headers = {
            "Content-Type": "application/form-data",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        self.url = "https://api.ecoledirecte.com/v3/login.awp?v=4.38.0"

        self.login()
    
    def login(self):
        json_data = json.dumps(self.data)
        credentials_valid = False

        while not credentials_valid:
            response = requests.post(self.url, data={'data': json_data}, headers=self.headers)

            if response.status_code == 200:
                json_response = json.loads(response.text)

                if json_response["code"] == 200:
                    print(f"You're logged as {self.identifiant}")

                    id = json_response["data"]["accounts"][0]["id"]
                    token = json_response["token"]
                    etablissement = json_response["data"]["accounts"][0]["nomEtablissement"]
                    credentials_valid = True

                    Main(id, token, self.identifiant, etablissement)

                elif json_response["code"] == 505:
                    print("Invalid username or password")
                    self.get_credentials()
            else:
                print(f"La requête a retourné le code d'état HTTP {response.status_code}")

class Main():
    def __init__(self, id, token, username, etablissement):
        self.commands = {
            "cd",
            "ls",
            "help"
        }

        self.main(id, token, username, etablissement)

    def main(self, id, token, username, etablissement):
        print(f"[{username}@{etablissement}]")

class Notes():
    def __init__(self, id, token):
        self.timestamp = 1625309472.357246
        self.date_time = datetime.fromtimestamp(self.timestamp)

        self.data = {
            "anneeScolaire": ""
        }

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "X-Token": token
        }
        #self.test(id, token)

        self.main()

        # A big mess :
    def test(self, id, token):
        self.url = f"https://api.ecoledirecte.com/v3/eleves/{id}/notes.awp?verbe=get&v=4.44.0"
        json_data = json.dumps(self.data)

        response = requests.post(self.url, data={'data': json_data}, headers=self.headers)
        self.json_response = json.loads(response.text)
        print(self.json_response)
        if self.json_response["code"] == 520:
            load_dotenv()
            url = "https://api.ecoledirecte.com/v3/login.awp?v=4.38.0"

            self.data = {
                "identifiant": os.getenv("USER"),
                "motdepasse": os.getenv("PASSWORD"),
                "isReLogin": False,
                "uuid": ""
            }

            self.headers = {
                "Content-Type": "application/form-data",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            }

            response = requests.post(self.url, data={'data': json_data}, headers=self.headers)

            if response.status_code == 200:
                    json_response = json.loads(response.text)

                    if json_response["code"] == 200:
                        id = json_response["data"]["accounts"][0]["id"]
                        token = json_response["token"]

                        print(os.environ["TOKEN"])  # outputs None
                        os.environ["TOKEN"] = token
                        print(os.environ['TOKEN'])  # outputs 'newvalue'

                    elif json_response["code"] == 505:
                        print("Invalid username or password")
                        self.get_credentials()
            else:
                print(f"La requête a retourné le code d'état HTTP {response.status_code}")


Login()
