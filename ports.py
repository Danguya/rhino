import socket


openPorts = []

def scan_port(host, begin=1, end=65535):
    white_space = " "
    try:
        print("[*] Escaneando {} ".format(end-begin+1)+"portas de {}".format(begin)+"-{}".format(end))
        for port in range(begin, end):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2)
            result = client.connect_ex((host, port))
            if result == 0:
                openPorts.append(port)
            client.close()
        if len(openPorts) <= 0:
            print("[-] Nenhuma porta está aberta")
        return openPorts
    except socket.error as sockError:
        print(sockError)
    return openPorts