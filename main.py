import requests
from datetime import datetime
import time
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
                    time.sleep(1.5)

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
            "clear",
            "exit",
            "logout",
            "help",
        }

        self.categories = {
            "Notes",
            "Messagerie",
            "EDT",
            "Agenda",
            "-help",

        }

        self.id = id
        self.token = token
        self.username = username
        self.etablissement = etablissement

        os.system('cls' if os.name == 'nt' else 'clear')

        self.main()

    def main(self):
        self.command = input(f"[{self.username}@{self.etablissement}] ")
        self.commandSeparators = self.command.split(" ",1)[0]
        self.check_command()

    def check_command(self):
        if self.commandSeparators in self.commands:
            if self.commandSeparators == "cd":
                self.cd()

            elif self.commandSeparators == "ls":
                self.ls()

            elif self.commandSeparators == "help":
                self.help()

            elif self.commandSeparators == "clear":
                self.clear()

            elif self.commandSeparators == "logout":
                self.logout()

            elif self.commandSeparators == "exit":
                self.exit()
                
        else:
            print(f"Command '{self.commandSeparators}' not found.")
            self.main()

    def cd(self):
        try:
            dir = self.command.split(" ",2)[1]
        except IndexError:
            print("Please specify the directory")
            self.main()

        if dir in self.categories:
            if dir == "Notes" or dir == "notes":
                print("Directory in dev...")
            elif dir == "Messagerie" or dir == "messagerie":
                print("Directory in dev...")
            elif dir == "EDT" or dir == "edt":
                print("Directory in dev...")
            elif dir == "Agenda" or dir == "agenda":
                print("Directory in dev...")
            elif dir == "-help":
                print("""DIR HELP :
                      The avalaible directories are : Notes, Messagerie, EDT, Agenda""")
        else:
            print(f"'{dir}' is not a valid directory, please type cd -help to see the correct directories")

        self.main()
    
    def ls(self):
        print("Command in dev ....")
        self.main()

    def help(self):
        print("""LIST OF COMMANDS :
              cd : Use it to change of category, see cd -help for more informations
              ls : See the contenue of the category (like grades, schedule)
              clear : Clear the terminal
              logout : Return to the login page
              exit : Exit the program""")
        self.main()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.main()

    def logout(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        Login()

    def exit(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)








































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
