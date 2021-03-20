from colorama import Fore, init
from os import system
from time import sleep
import json
init()
system("cls")


print(" __  __ _       _       ____        _        ____\n|  \/  (_)_ __ (_)     |  _ \  __ _| |_ __ _| __ )  __ _ ___  ___\n| |\/| | | '_ \| |_____| | | |/ _` | __/ _` |  _ \ / _` / __|/ _ \ \n| |  | | | | | | |_____| |_| | (_| | || (_| | |_) | (_| \__ \  __/\n|_|  |_|_|_| |_|_|     |____/ \__,_|\__\__,_|____/ \__,_|___/\___|\n")

def Reset_Var():
    name = ""
    family = ""
    website = ""
    i = 0


def Write_Database(item, filename="People.json"):
    with open(filename, 'w') as f:
        json.dump(item, f, indent=4)


def Add_Person(id, name, family, website):
    data = {}
    data['id'] = id
    data['name'] = name
    data['family'] = family
    data['website'] = website


def main():
    name = ""
    family = ""
    website = ""
    Selected_ID = ""
    Index = 0
    data = {}
    i = 0
    while True:

        print(Fore.RED+"["+Fore.YELLOW+"1"+Fore.RED+"]"+Fore.GREEN+" Add New Person\n" +
              Fore.RED+"["+Fore.YELLOW+"2"+Fore.RED+"]"+Fore.GREEN+" Read Database\n" +
              Fore.RED+"["+Fore.YELLOW+"3"+Fore.RED+"]"+Fore.GREEN+" Delete Person\n" +
              Fore.RED+"["+Fore.YELLOW+"4"+Fore.RED+"]"+Fore.GREEN+" Edit Person\n" +
              Fore.RED+"["+Fore.YELLOW+"5"+Fore.RED+"]"+Fore.GREEN+" Exit\n")

        Option = input(Fore.RED+"Select Option : ")

        if Option == "1":
            Count = int(input("Count Add Person? "))
            while Count == 0:
                print(f"You can't add {Count} Person")
                Count = int(input("Count Add Person? "))

            while i < Count:
                print(Fore.CYAN+f"Add Person [{i+1}]")
                name = input("Name : ")
                family = input("Family : ")
                website = input("Website : ")
                with open('People.json') as outfile:
                    Database = json.load(outfile)
                    People = Database['People']
                    data['id'] = Database['Key']
                    data['name'] = name
                    data['family'] = family
                    data['website'] = website
                    People.append(data)
                    k = int(Database['Key'])
                    k += 1
                    Database['Key'] = str(k)
                Write_Database(Database)
                name = ""
                family = ""
                website = ""
                i += 1

            outfile.close()

            print(Fore.GREEN+"Successfully\n")
            i = 0
            data = {}
            continue

        if Option == "2":
            with open('People.json') as json_file:
                Read = json.load(json_file)
                for p in Read['People']:
                    print(Fore.GREEN+'ID: ' + Fore.CYAN+p['id'])
                    print(Fore.GREEN+'Name: ' + Fore.CYAN+p['name'])
                    print(Fore.GREEN+'Family: ' + Fore.CYAN+p['family'])
                    print(Fore.GREEN+'Website: ' + Fore.CYAN+p['website'])
                    print(
                        Fore.RED+'***************************************************')

            print(Fore.GREEN+"Successfully\n")
            continue

        if Option == "3":
            with open('People.json') as json_file:
                Read = json.load(json_file)
                for p in Read['People']:
                    print(Fore.GREEN+'ID: ' + Fore.CYAN+p['id'])
                    print(Fore.GREEN+'Name: ' + Fore.CYAN+p['name'])
                    print(Fore.GREEN+'Family: ' + Fore.CYAN+p['family'])
                    print(Fore.GREEN+'Website: ' + Fore.CYAN+p['website'])
                    print(
                        Fore.RED+'***************************************************')
            Selected_ID = str(input("Enter ID of Person Delete : "))
            with open('People.json') as json_file:
                Database = json.load(json_file)
                People = Database['People']

                for item in People:
                    if item['id'] == Selected_ID:
                        del People[Index]
                    else:
                        Index += 1

                Write_Database(Database)
                print(Fore.GREEN+"Successfully\n")
                Index = 0
                Selected_ID = 0
                continue

        if Option == "4":
            with open('People.json') as json_file:
                Read = json.load(json_file)
                for p in Read['People']:
                    print(Fore.GREEN+'ID: ' + Fore.CYAN+p['id'])
                    print(Fore.GREEN+'Name: ' + Fore.CYAN+p['name'])
                    print(Fore.GREEN+'Family: ' + Fore.CYAN+p['family'])
                    print(Fore.GREEN+'Website: ' + Fore.CYAN+p['website'])
                    print(
                        Fore.RED+'***************************************************')
            Selected_ID = str(input("Enter ID of Person Update : "))
            with open('People.json') as json_file:
                Database = json.load(json_file)
                People = Database['People']

                for item in People:
                    if item['id'] == Selected_ID:
                        print(f"{item['name']} {item['family']} Selected")
                        item['name'] = str(input("Name : "))
                        item['family'] = str(input("Family : "))
                        item['website'] = str(input("Website : "))

                Write_Database(Database)
                print(Fore.GREEN+"Successfully\n")
                Selected_ID = 0
                continue

        if Option == "5":
            print(Fore.RED+"Exited")
            sleep(2)
            break


try:
	main()
except:
	print(Fore.RED+"Exit")
	sleep(1)
