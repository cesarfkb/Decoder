import tkinter as tk
from tkinter import messagebox

ERROS = {'NUMERICO': 'Erro: o código digitado não é válido. O código não pode conter letras ou símbolos.',
         'BINARIO': 'Erro: o código digitado não é válido. O código deve conter apenas 0s e 1s.',
         'TAMANHO': 'Erro: o código digitado não é válido. O código deve ter um tamanho múltiplo de 32.',
         'VAZIO': 'Erro: o código digitado não é válido. O código não pode estar vazio.'}

def tela_erro(mensagem: str):
    mensagem = ERROS.get(mensagem, mensagem)
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Erro', mensagem)
    root.destroy()
    
if '__main__' == __name__:
    tela_erro("Erro: o código digitado não é válido.")