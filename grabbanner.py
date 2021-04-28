import socket
listBanners = []
def getBanners(host, openPorts):
    
    try:
        for port in openPorts:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2)
            client.connect((str(host), int(port)))
            listBanners.append(client.recv(1024).decode())
            client.close()
            return
    except socket.error as sockError:
        print(sockError)
    return listBanners