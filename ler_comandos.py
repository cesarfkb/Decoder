COMANDOS_R = {('0100000', '000'): 'SUB', ('0000000', '000'): 'ADD',
              ('0000000', '001'): 'SLL', ('0000000', '010'): 'SLT'}
COMANDOS_I = {'000': 'ADDI'}
COMANDOS_S = {'000': 'SB', '001': 'SH', '010': 'SW'}
OPCODES = {51: 'R', 3: 'I', 35: 'S', 99: 'SB'}

def ler_comandos(codigo: str) -> list:
    opcode = get_opcode(codigo)
    match(opcode):
        case 'R':
            return get_comando_r(codigo)
        case 'I':
            return get_comando_i(codigo)
        case 'S':
            return get_comando_s(codigo)
        case _:
            return '1'

def get_opcode(codigo: str) -> str:
    return OPCODES.get(int(codigo[-7:], 2))

def get_comando_r(linha: str) -> list:
    funct7 = linha[0:7]
    rs2 = linha[7:12]
    rs1 = linha[12:17]
    funct3 = linha[17:20]
    rd = linha[20:25]
    
    if COMANDOS_R.get((funct7, funct3)) is None:
        return '2'
    
    return ['R', COMANDOS_R.get((funct7, funct3)), hex(int(rs1, 2)), hex(int(rs2, 2)), hex(int(rd, 2))]

def get_comando_i(linha: str) -> list:
    imm = linha[0:12]
    rs1 = linha[12:17]
    funct3 = linha[17:20]
    rd = linha[20:25]
    
    if COMANDOS_I.get(funct3) is None:
        return '2'
    
    return ['I', COMANDOS_I.get(funct3), hex(int(rs1, 2)), hex(int(rd, 2)), int(imm, 2)]

def get_comando_s(linha: str) -> list:
    imm = linha[0:12]
    rs2 = linha[12:17]
    rs1 = linha[17:22]
    funct3 = linha[22:25]
    
    if COMANDOS_S.get(funct3) is None:
        return '2'
    
    return ['S', COMANDOS_S.get(funct3), hex(int(rs1, 2)), hex(int(rs2, 2)), int(imm, 2)]

