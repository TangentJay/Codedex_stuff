#This es a basic port scanner. Low tier.

import socket # teh scoket module that allows us to creat network conecctions


def Low_Tier_scanner(host, ports):
    print(f'scanning {host}')


    #we loop through ports in the list
    #AF_INET=IPv4 address
    for port in ports:
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sock stream is TCP| SOCK DGRAM ist UDP
        so.settimeout(0.5)# set time out after .5

        try:
            so.connetc((host,port))
            print(f'el port {port} es open')
        except:
            print(f'das port {port} ist nicht offen')
        finally:
            so.close()


Mi_host = '127.0.0.1' #this is teh local host
some_ports = [21, 22, 80, 433] # FTP, SSH, HTTP und HTTPS

Low_Tier_scanner(Mi_host, some_ports)

