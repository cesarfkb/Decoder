import re
import tkinter as tk
from tkinter import filedialog, scrolledtext

def tela_entrada() -> str:
    
    codigo = []
    
    def carregar_arquivo():
        caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo de texto", filetypes=[("Arquivos de texto", "*.txt")])
        if caminho_arquivo:
            with open(caminho_arquivo, 'r') as arquivo:
                area_texto.delete(1.0, tk.END)
                area_texto.insert(tk.END, arquivo.read())
            
    def submeter_codigo() -> str:
        codigo.append(area_texto.get(1.0, tk.END).strip())
        root.destroy()
    
    root = tk.Tk()
    root.title("Digite o código ou carregue um arquivo")
    
    area_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
    area_texto.pack(padx=10, pady=10)
    
    carregar_arquivo = tk.Button(root, text="Carregar arquivo", command=carregar_arquivo)
    carregar_arquivo.pack(side=tk.LEFT, padx=10, pady=10)
    
    submeter_codigo = tk.Button(root, text="Submeter código", command=submeter_codigo)
    submeter_codigo.pack(side=tk.RIGHT, padx=10, pady=10)
    
    root.mainloop()
    
    return codigo[0] if codigo else None

# root = tk.Tk()
# root.title("Digite o código ou carregue um arquivo")

if '__main__' == __name__:
    teste = tela_entrada()
    print(teste)
