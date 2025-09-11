import socket


def Low_tier_scanner2(host):
    print(f'scanning host {host} ports 1~500')

    offen_portz = []
    # bannerz = {}
    totalScanned = 0


    for port in range(1,501): #we will scan up to 500 for now

        xo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xo.settimeout(.01)#made time out shortter to reduce time spent scanning


        try:
            xo.connect((host, port))
            print(f'Port {port} is OPEN')
            offen_portz.append(port)


        except:
             if port % 10 == 0:

                print(f'das port {port} ist nicht offen')

        finally:
            xo.close()
        totalScanned += 1


    print(f'total ports scanned {totalScanned}')

    print(f'number of open ports {len(offen_portz)}')
    print(f'open ports are: {offen_portz}')


localH = '127.0.0.1'

Low_tier_scanner2(localH)

