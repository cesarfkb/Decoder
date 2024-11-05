import tkinter as tk


def tela_detalhes(comandos: list) -> None:
    
    lista_comandos = ''
    count = 1
    
    for comando in comandos:
        lista_comandos += f'{count} - {comando}\n'
        count += 1
    
    def done():
        root.destroy()
        
    root = tk.Tk()
    root.title("Detalhes Comandos")
    
    commands_label = tk.Label(root, text="Comandos Executados" + "\n" + lista_comandos)
    commands_label.pack(pady=10)
    
    done_button = tk.Button(root, text="Fechar", command=done)
    done_button.pack(side=tk.LEFT, padx=20, pady=20)
    
    root.geometry("400x400")
    
    root.mainloop()