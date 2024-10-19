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
        
def executar_comando_r(comandos: list) -> None:
    rs2 = comandos[3]
    rs2_dado = verificar_memoria(rs2)
    rs1 = comandos[2]
    rs1_dado = verificar_memoria(rs1)
    rd = comandos[4]
    
    match(comandos[1]):
        case 'ADD':
            memoria[rd] = rs1_dado + rs2_dado
            print(f'ADD {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SUB':
            memoria[rd] = rs1_dado - rs2_dado
            print(f'SUB {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SLL':
            memoria[rd] = rs1_dado << rs2_dado
            print(f'SLL {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SLT':
            memoria[rd] = 1 if rs1_dado < rs2_dado else 0
            print(f'SLT {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case _:
            return None
        
def executar_comando_i(comandos: list) -> None:
    imm = comandos[4]
    rs1 = comandos[2]
    rs1_dado = verificar_memoria(rs1)
    rd = comandos[3]
    match(comandos[1]):
        case 'ADDI':
            memoria[rd] = rs1_dado + imm
            print(f'ADDI {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
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