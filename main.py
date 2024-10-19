from tela_entrada_dados import tela_entrada
from tela_erro import tela_erro
import tratamento_codigo

if '__main__' == __name__:
    codigo = tela_entrada()
    if codigo is None:
        exit()
        
    while not tratamento_codigo.validar_codigo(codigo)[0]:
        tela_erro(tratamento_codigo.validar_codigo(codigo)[1])
        codigo = tela_entrada()
        
    print(codigo)