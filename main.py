from tela_entrada_dados import tela_entrada
from tela_erro import tela_erro
import tratamento_codigo
from ler_comandos import ler_comandos
from executar_comandos import executar_comandos

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
        executar_comandos(comando)
        