import re
from utils_comandos import *
# codigo="00000000001100010000001110110011\n01000000101100111000011110110011\n00000000111111011001010100110011\n00000000101110010010100110110011\n00000001100101110100011000110011\n00000001111011010110011100110011\n00000001010010010111101110110011\n00000000001000011010010010000011\n00000011101101111010000010100011\n00000000001100001000000001100011\n00000000001100010000001110110011\n00000000001100010000001110110011"
codigo = "00000000011000010000000010000011\n00000000000100010000000100110011\n00000000000100010000000100110011\n01000000000100010000000110110011"

codigo = codigo.replace('\n', '')
bits = []
memoria = {}


def valida_codigo(codigo: str):
    pattern = r'^[^0-2]*$|^[0-1]*$'
    if codigo.isnumeric and bool(re.match(pattern, codigo)) and (len(codigo) % 32 == 0):
        return True
    else:
        return False


def separar_codigo(codigo: str):
    ops = []
    while codigo:
        ops.append(codigo[:32])
        codigo = codigo[32:]
    return ops


def converter_binario(codigo: str):
    decimal = 0
    for digit in codigo:
        decimal = decimal*2 + int(digit)
    return decimal


def get_opcode(codigo: str):
    return converter_binario(codigo[-7:])


def verificar_memoria(endereco: int):
    if endereco not in memoria:
        memoria[endereco] = 0


def ler_func_r(linha: str):
    funct7 = linha[:7]
    rs2 = linha[7:12]
    verificar_memoria(converter_binario(rs2))
    rs1 = linha[12:17]
    verificar_memoria(converter_binario(rs1))
    funct3 = linha[17:20]
    rd = linha[20:25]
    verificar_memoria(converter_binario(rd))
    comando = (funct7, funct3)
    print(COMANDOS_R.get(comando), "rs1:", converter_binario(rs1),
          "rs2:", converter_binario(rs2), "rd:", converter_binario(rd))
    executar_comando_r(comando, converter_binario(
        rs1),  converter_binario(rs2),  converter_binario(rd))


def executar_comando_r(comando: tuple, rs1: int, rs2: int, rd: int):
    match (COMANDOS_R.get(comando)):
        case 'SUB':
            memoria[rd] = memoria[rs1] - memoria[rs2]
        case 'ADD':
            memoria[rd] = memoria[rs1] + memoria[rs2]
        case 'SLL':
            memoria[rd] = memoria[rs1] << memoria[rs2]
        case 'SLT':
            memoria[rd] = memoria[rs1] < memoria[rs2]


def ler_func_i(linha: str):
    imm = linha[:12]
    rs1 = linha[12:17]
    verificar_memoria(converter_binario(rs1))
    funct3 = linha[17:20]
    rd = linha[20:25]
    verificar_memoria(converter_binario(rd))
    comando = funct3
    print(COMANDOS_I.get(comando), "rs1:", converter_binario(rs1),
          "rd:", converter_binario(rd), "imm:", converter_binario(imm))
    executar_comando_i(comando, converter_binario(
        rs1), converter_binario(rd), converter_binario(imm))


def executar_comando_i(comando: str, rs1: int, rd: int, imm: int):
    match (COMANDOS_I.get(comando)):
        case 'ADDI':
            memoria[rd] = memoria[rs1] + imm


def ler_func_s(linha: str):
    imm = linha[:7]
    rs2 = linha[7:12]
    verificar_memoria(converter_binario(rs2))
    rs1 = linha[12:17]
    verificar_memoria(converter_binario(rs1))
    funct3 = linha[17:20]
    imm2 = linha[20:25]


def ler_linha(linha: str):
    match (OPCODES.get(get_opcode(linha))):
        case 'R':
            ler_func_r(linha)
        case 'I':
            ler_func_i(linha)
        case 'S':
            ler_func_s(linha)
        case 'SB':
            print('SB')


ops = separar_codigo(codigo)
for linha in ops:
    ler_linha(linha)
print(memoria)
