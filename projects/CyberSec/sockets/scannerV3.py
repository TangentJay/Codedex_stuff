import socket
# import time
from tqdm import tqdm
from colorama import Fore
from tkinter import *
from tkinter import ttk


def Low_tier_scanner2(host, start, stop):
    print(f'scanning host {host}, ports {start}~{stop}')

    offen_portz = []
    # bannerz = {}
    totalScanned = 0


    for port in tqdm(range(start, stop +1), desc="scanning", unit='Port', colour='cyan'): 

        xo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xo.settimeout(.01)#made time out shortter to reduce time spent scanning


        try:
            xo.connect((host, port))
            print(Fore.LIGHTMAGENTA_EX + f'\nPort {port} is OPEN'+ Fore.RESET) # comma vs concatenate
            offen_portz.append(port)


        except:
            #  if port % 10 == 0:

            #     print(f'das port {port} ist nicht offen')
            pass

        finally:
            xo.close()
        totalScanned += 1


    print(f'total ports scanned = {totalScanned}')

    
    if len(offen_portz)> 0:
        print(Fore.LIGHTYELLOW_EX +f'number of open ports: {len(offen_portz)} and the open ports are: {offen_portz}')
    else:
        print('No ports are open')

# localH = '127.0.0.1'



hostz = input('eingeben host IP or leave blank for Default: ') or '127.0.0.1'
start = int(input('eingeben start port to scan: '))
end = int(input('eingeben end point to scan: '))

Low_tier_scanner2(hostz, start, end)