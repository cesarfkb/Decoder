import tkinter as tk
from tkinter import messagebox

from tela_detalhes import tela_detalhes

def tela_resultados(comandos: list, memoria: list, formatado: list) -> None:
    def done():
        root.destroy()
        
    def see_details():
        tela_detalhes(formatado)
        
    root = tk.Tk()
    root.title("Resultado Decoder")
    
    commands_label = tk.Label(root, text="Comandos Executados" + "\n" + str(comandos))
    commands_label.pack(pady=10)
    
    memory_label = tk.Label(root, text="Memória Final" + "\n" + str(memoria[-1]))
    memory_label.pack(pady=10)
    
    done_button = tk.Button(root, text="Fechar", command=done)
    done_button.pack(side=tk.LEFT, padx=20, pady=20)
    
    see_details_button = tk.Button(root, text="Ver Detalhes", command=see_details)
    see_details_button.pack(side=tk.RIGHT, padx=20, pady=20)
    
    root.mainloop()
    