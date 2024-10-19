import re

def validar_codigo(codigo: str) -> tuple:
    if not codigo.isnumeric():
        return False, 'NUMERICO'
    elif not re.match(r'^[01]+$', codigo):
        return False, 'BINARIO'
    elif len(codigo) % 32 != 0:
        return False, 'TAMANHO'
    elif not codigo:
        return False, 'VAZIO'
    
    return True, None

def separar_codigo(codigo: str) -> list:
    return [codigo[i:i+32] for i in range(0, len(codigo), 32)]