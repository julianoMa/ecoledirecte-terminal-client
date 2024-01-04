import requests
import time
import getpass
import json
import string
import os

commands = {
            "cd",
            "ls",
            "clear",
            "exit",
            "logout",
            "help",
            "",
}

categories = {
            "Accueil",
            "Notes",
            "Messagerie",
            "EDT",
            "Agenda",
            "-help",
}

def remove_non_printable(text):
    return ''.join(filter(lambda x: x in string.printable, text))

def check_command(commandSeparators, id, token, username, etablissement, command, dir):
        if commandSeparators in commands:
            if commandSeparators == "cd":
                cd(id, token, username, etablissement, command)
            elif commandSeparators == "ls":
                ls(dir, id, token)
            elif commandSeparators == "help":
                help()
            elif commandSeparators == "clear":
                clear()
            elif commandSeparators == "logout":
                logout()
            elif commandSeparators == "exit":
                exit()
            elif commandSeparators == "":
                pass
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

def ls(dir, id, token):
        if dir == "Main":
            print("There's nothing to show here... yet")
        elif dir == "Notes":
            url = f"https://api.ecoledirecte.com/v3/eleves/{id}/notes.awp?verbe=get&v=4.46.3"
            
            data = {
                "anneeScolaire": ""
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "X-Token": token
            }
    
            json_data = json.dumps(data)

            response = requests.post(url, data={'data': json_data}, headers=headers)
            response = response.json()  

            # Getting the periodes

            periodes = ["A001", "A002", "A003"]

            periodes_names = []

            for periode_data in response["data"]["periodes"]:
                id_periode = periode_data["idPeriode"]
                if id_periode in periodes:
                    periode_name = periode_data["periode"]
                    periodes_names.append(periode_name)

            # Getting the subjects
                    
            subjects = []

            for periode_data in response["data"]["periodes"][0]["ensembleMatieres"]["disciplines"]:
                discipline = periode_data["discipline"]
                subjects.append(discipline)


            # Getting the grades for each subject
        
            # Initialize subject_values to store grades for each subject and period
            subject_values = {subject: {p: [] for p in periodes} for subject in subjects}

            # Iterate through notes and collect values by subject and period
            for note in response["data"]["notes"]:
                subject = note["libelleMatiere"]
                valeur = note["valeur"]
                periode = note["codePeriode"]

                # Check if the period and subject are in the expected lists
                if periode in periodes and subject in subject_values:
                    subject_values[subject][periode].append(valeur)

            # Displaying values by subject aligned with periods
            max_len = max(len(subject) for subject in subject_values.keys())

            # Calculate maximum widths for each column
            column_widths = [max(len(period), max(len(str(grade)) if str(grade) != 'Disp' else len('Disp') for grade in values.values())) for period, values in zip(periodes_names, subject_values.values())]

            print(f"{'Subject':<{max_len}} | {' | '.join([f'{p:^{w}}' for p, w in zip(periodes_names, column_widths)])}")

            for subject, values in subject_values.items():
                grades = []
                for period, grade in values.items():
                    if str(grade) == 'Disp':
                        grades.append('Disp')
                    else:
                        grades.append(", ".join(map(str, grade)) if isinstance(grade, list) else str(grade))

                # Output each row with proper spacing
                print(f"{subject:<{max_len}} | {' | '.join([f'{g:^{w}}' for g, w in zip(grades, column_widths)])}")

        elif dir == "Messagerie":
            print("Can't access to your mails")
        elif dir == "Agenda":
            print("Can't access to your schedule")

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
    quit()

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
        self.password = getpass.getpass(f"{self.identifiant}'s password : ")

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
                    time.sleep(1)
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
        check_command(commandSeparators, self.id, self.token, self.username, self.etablissement, self.command, self.dir)

        self.main()

class Notes():
    def __init__(self, id, token, username, etablissement):
        self.dir = "Notes"

        self.id = id
        self.token = token
        self.username = username
        self.etablissement = etablissement

        self.url = f"https://api.ecoledirecte.com/v3/eleves/{self.id}/notes.awp"

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
        check_command(commandSeparators, self.id, self.token, self.username, self.etablissement, self.command, self.dir)

        self.main()

Login()