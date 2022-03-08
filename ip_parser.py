import requests
from colorama import init
init(autoreset=True)
from colorama import Fore, Back
from pyfiglet import Figlet


def info_ip(ip='127.0.0.1'):
    try:
        a = Fore.GREEN
        b = Fore.RED
        r = requests.get(f"http://ip-api.com/json/{ip}") 
        data = r.json()

        city = data['city']
        country = data['country']
        ip = data['query']
        regionname = data['regionName']
        lat = data['lat']
        lon = data['lon']
        isp = data['isp']

        
        print("\n",a +f"[!] Data for this IP - {ip}\n",
              b +"<--------------------------------->\n",
              a +f"[+] Geolocation - {city}, {regionname}, {country}\n",
              b +"<--------------------------------->\n",
              a +f"[+] Coordinates - [LAT] = {lat}, [LON] = {lon}\n",
              b +"<--------------------------------->\n",
              a + f"[+] Provider - {isp}"
            )

    except Exception as ex:
        print(Fore.RED + '[-] Incorrect IP entered or no internet access!')

def main():
    preview_text = Figlet(font='slant')
    print(Fore.CYAN + preview_text.renderText("SCRENCIL-IP"))
    print(Fore.BLUE + "<<<created by screncil>>>")
    print()
    ip = input("ENTER YOUR IP >>> ")
    info_ip(ip)
    

if __name__ == '__main__':
    main()