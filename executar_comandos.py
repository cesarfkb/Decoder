memoria = {}

def verificar_memoria(endereco: int) -> int:
    if endereco not in memoria:
        memoria[endereco] = 0
        
    return memoria[endereco]

def executar_comandos(comandos: list) -> None:
    type_comando = comandos[0]
    match(type_comando):
        case 'R':
            executar_comando_r(comandos)
        case 'I':
            executar_comando_i(comandos)
        case 'S':
            executar_comando_s(comandos)
        case _:
            return None
        
def executar_comando_r(comando: list) -> None:
    match(comando[1]):
        case 'ADD':
            print(f'ADD {comando[2]}, {comando[3]}, {comando[4]}')
        case 'SUB':
            print(f'SUB {comando[2]}, {comando[3]}, {comando[4]}')
        case 'SLL':
            print(f'SLL {comando[2]}, {comando[3]}, {comando[4]}')
        case 'SLT':
            print(f'SLT {comando[2]}, {comando[3]}, {comando[4]}')
        case _:
            return None
        
def executar_comando_i(comando: list) -> None:
    match(comando[1]):
        case 'ADDI':
            print(f'ADDI {comando[2]}, {comando[3]}, {comando[4]}')
        case _:
            return None
        
def executar_comando_s(comando: list) -> None:
    match(comando[1]):
        case 'SB':
            print(f'SB {comando[2]}, {comando[3]}, {comando[4]}')
        case 'SH':
            print(f'SH {comando[2]}, {comando[3]}, {comando[4]}')
        case 'SW':
            print(f'SW {comando[2]}, {comando[3]}, {comando[4]}')
        case _:
            return None