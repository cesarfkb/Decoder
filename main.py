from tela_entrada_dados import tela_entrada
from tela_erro import tela_erro
from tela_resultados import tela_resultados
from executar_comandos import executar_comandos
from ler_comandos import ler_comandos
import tratamento_codigo

historico_comandos = []
historico_comandos_formatados = []
historico_memoria = []

if '__main__' == __name__:
    codigo = tela_entrada()
    
    if codigo is None:
        exit()
    
    codigo = codigo.replace('\n', '')
        
    while not tratamento_codigo.validar_codigo(codigo)[0]:
        tela_erro(tratamento_codigo.validar_codigo(codigo)[1])
        codigo = tela_entrada()
    
    linhas_codigo = tratamento_codigo.separar_codigo(codigo)
    
    for linha in linhas_codigo:
        comando = ler_comandos(linha)
        
        if comando == '1':
            tela_erro('OPCODE')
            continue
        elif comando == '2':
            tela_erro('FUNC')
            continue
            
        historico_comandos.append(comando)
        tupla_resposta = executar_comandos(comando)
        
        if tupla_resposta is None or tupla_resposta[1] is None:
            tela_erro('GENERIC')
            continue
        
        (memoria, ultimo_comando) = tupla_resposta
        
        historico_comandos_formatados.append(ultimo_comando)
        historico_memoria.append(memoria)
        
    tela_resultados(historico_comandos, historico_memoria, historico_comandos_formatados)
        
    
        