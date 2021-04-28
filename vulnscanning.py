import os
import database.vuln



def checkDatabase():
    filename = "./database/vulnerabilities.txt"


    if not os.path.isfile(filename):
        print("[!] Banco de vulnerabilidades não encontrado")
        return(0)

    elif not os.access(filename, os.R_OK):
        print("[!] Acesso negado ao ler o banco de vulnerabilidades")
        return(0)
        
    return filename


def scan(content):
    vulnerabilidades_encontrada = {}
    for vuln in database.vuln.vulns:
        if content == vuln['Name']:
            vulnerabilidades_encontrada = vuln
        
    return vulnerabilidades_encontrada

def info(name):
    result = {}
    
    for vuln in database.vuln.vulns:
        if name in vuln['Name']:
            return vuln
        
    return result

