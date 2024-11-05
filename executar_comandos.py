memoria = {}
ultimo_comando = ''

def verificar_memoria(endereco: int) -> int:
    if endereco not in memoria:
        memoria[endereco] = 0
        
    return memoria[endereco]

def executar_comandos(comandos: list) -> tuple:
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
        
    return (memoria, ultimo_comando)
        
def executar_comando_r(comandos: list) -> None:
    global ultimo_comando
    
    rs2 = comandos[3]
    rs2_dado = verificar_memoria(rs2)
    rs1 = comandos[2]
    rs1_dado = verificar_memoria(rs1)
    rd = comandos[4]
    
    match(comandos[1]):
        case 'ADD':
            memoria[rd] = rs1_dado + rs2_dado
            # print(f'ADD {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SUB':
            memoria[rd] = rs1_dado - rs2_dado
            # print(f'SUB {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SLL':
            memoria[rd] = rs1_dado << rs2_dado
            # print(f'SLL {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'SLT':
            memoria[rd] = 1 if rs1_dado < rs2_dado else 0
            # print(f'SLT {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'XOR':
            memoria[rd] = rs1_dado ^ rs2_dado
        case 'OR':
            memoria[rd] = rs1_dado | rs2_dado
        case 'AND':
            memoria[rd] = rs1_dado & rs2_dado
        case _:
            ultimo_comando = None
            return
        
    
    ultimo_comando = f'[{comandos[0]}-type {comandos[1]}]\nrs1: {rs1} valor atual: {rs1_dado}\nrs2: {rs2} valor atual: {rs2_dado}\nrd: {rd} -> {memoria[rd]}'
        
    
        
def executar_comando_i(comandos: list) -> None:
    global ultimo_comando
    
    imm = comandos[4]
    rs1 = comandos[2]
    rs1_dado = verificar_memoria(rs1)
    rd = comandos[3]
    
    match(comandos[1]):
        case 'ADDI':
            memoria[rd] = rs1_dado + imm
            # print(f'ADDI {comandos[2]}, {comandos[3]}, {comandos[4]}\n {memoria}')
        case 'XORI':
            memoria[rd] = rs1_dado ^ imm
        case 'ORI':
            memoria[rd] = rs1_dado | imm
        case 'ANDI':
            memoria[rd] = rs1_dado & imm
        case _:
            ultimo_comando = None
            return
        
    ultimo_comando = f'[{comandos[0]}-type {comandos[1]}]\nrs1: {rs1} valor atual: {rs1_dado}\nimm: {imm}\nrd: {rd} -> {memoria[rd]}'
        
def executar_comando_s(comandos: list) -> None:
    global ultimo_comando
    
    imm = comandos[4]
    rs2 = comandos[3]
    rs2_dado = verificar_memoria(rs2)
    rs1 = comandos[2]
    rs1_dado = verificar_memoria(rs1)
    
    
    match(comandos[1]):
        case 'SB':
            memoria[rs1_dado + imm] = rs2_dado
        case 'SH':
            memoria[rs1_dado + imm] = rs2_dado
        case 'SW':
            memoria[rs1_dado + imm] = rs2_dado
        case _:
            return None