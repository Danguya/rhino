def errorHandler(typeError):
    messageError = ''
    if typeError == 111:
        messageError = "[-] Conexão recusada ou host indisponível"
        return messageError
    if typeError == OverflowError:
        messageError = "[!] As portas devem estar no intervalo 1-65535"
        return messageError
    else:
        return typeError