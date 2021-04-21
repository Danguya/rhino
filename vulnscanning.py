import os

vulnerabilidades_encontrada = []

def checkDatabase():
    filename = "./database/vulnerabilities.txt"


    if not os.path.isfile(filename):
        print("[!] Banco de vulnerabilidades não encontrado")
        return(0)

    elif not os.access(filename, os.R_OK):
        print("[!] Acesso negado ao ler o banco de vulnerabilidades")
        return(0)
        
    return filename


def scanVuln(content):
    filename = checkDatabase()
    database = open(filename,"r")
    for line in database.readlines():
        if line.strip("\n") in content:
            vulnerabilidades_encontrada.append(content.strip("\n"))

    return vulnerabilidades_encontrada

