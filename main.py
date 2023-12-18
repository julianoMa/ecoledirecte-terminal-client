import requests
from datetime import datetime
import time
import json
from dotenv import load_dotenv
import os

commands = {
            "cd",
            "ls",
            "clear",
            "exit",
            "logout",
            "help",
}

categories = {
            "Accueil",
            "Notes",
            "Messagerie",
            "EDT",
            "Agenda",
            "-help",
}

def check_command(commandSeparators, id, token, username, etablissement, command):
        if commandSeparators in commands:
            if commandSeparators == "cd":
                cd(id, token, username, etablissement, command)

            elif commandSeparators == "ls":
                ls(dir)

            elif commandSeparators == "help":
                help()

            elif commandSeparators == "clear":
                clear()

            elif commandSeparators == "logout":
                logout()

            elif commandSeparators == "exit":
                exit()
                
        else:
            print(f"Command '{commandSeparators}' not found.")

def cd(id, token, username, etablissement, command):
        try:
            dir = command.split(" ", 2)[1].lower()
        except IndexError:
            Main(id, token, username, etablissement)

        if dir in [category.lower() for category in categories]:
            if dir == "notes":
                Notes(id, token, username, etablissement)
            elif dir == "messagerie":
                print("Directory 'Messagerie' in dev...")
            elif dir == "edt":
                print("Directory 'EDT' in dev...")
            elif dir == "agenda":
                print("Directory 'Agenda' in dev...")
            elif dir == "-help":
                print("""DIR HELP DIRECTORIES:
                    The available directories are: Notes, Messagerie, EDT, Agenda""")
            elif dir == "accueil":
                Main(id, token, username, etablissement)
        else:
            print(f"'{dir.capitalize()}' is not a valid directory. Please type 'cd -help' to see the correct directories")

def ls():
        print("Command in dev ....")

def help():
    print("""LIST OF COMMANDS :
          cd : Use it to change of category, see cd -help for more informations
          ls : See the contenue of the category (like grades, schedule)
          clear : Clear the terminal
          logout : Return to the login page
          exit : Exit the program""")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logout():
    os.system('cls' if os.name == 'nt' else 'clear')
    Login()

def exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

class Login():
    def __init__(self):
        try:
            internet_check = requests.get("https://google.com")
        except requests.ConnectionError:
            print("Look like you're not connected to the Internet, please check your Internet connection before restarting the program ...")
            quit()
            
        self.get_credentials()

    def get_credentials(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
                    time.sleep(1)

                    id = json_response["data"]["accounts"][0]["id"]
                    token = json_response["token"]
                    etablissement = json_response["data"]["accounts"][0]["nomEtablissement"]
                    credentials_valid = True

                    os.system('cls' if os.name == 'nt' else 'clear')
                    Main(id, token, self.identifiant, etablissement)

                elif json_response["code"] == 505:
                    print("Invalid username or password")
                    self.get_credentials()
            else:
                print(f"La requête a retourné le code d'état HTTP {response.status_code}")

class Main():
    def __init__(self, id, token, username, etablissement):
        self.dir = "Main"

        self.id = id
        self.token = token
        self.username = username
        self.etablissement = etablissement

        self.directory = f"[{self.username}@{self.etablissement}] $ "

        self.main()

    def main(self):
        self.command = input(self.directory)
        commandSeparators = self.command.split(" ",1)[0]
        check_command(commandSeparators, self.id, self.token, self.username, self.etablissement, self.command)

        self.main()

class Notes():
    def __init__(self, id, token, username, etablissement):
        self.timestamp = time.time()
        self.date_time = datetime.fromtimestamp(self.timestamp)

        self.dir = "Notes"

        self.id = id
        self.token = token
        self.username = username
        self.etablissement = etablissement

        self.url = f"https://api.ecoledirecte.com/v3/eleves/{self.id}/notes.awp?verbe=get&v=4.44.0"

        self.data = {
            "anneeScolaire": ""
        }

        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "X-Token": self.token
        }

        self.directory = f"[{self.username}@{self.etablissement}/notes] $ "

        self.main()

    def main(self):
        self.command = input(self.directory)
        commandSeparators = self.command.split(" ",1)[0]
        check_command(commandSeparators, self.id, self.token, self.username, self.etablissement, self.command)

        self.main()

Login()