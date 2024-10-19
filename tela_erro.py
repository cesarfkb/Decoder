import tkinter as tk
from tkinter import messagebox

def tela_erro(mensagem: str):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Erro", mensagem)
    root.destroy()
    
if '__main__' == __name__:
    tela_erro("Erro: o código digitado não é válido.")