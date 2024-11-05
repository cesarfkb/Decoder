# Decoder
A aplicação decodifica instruções binárias e realiza uma simulação de sua execução. O programa utiliza uma interface de usuário para escrever ou realizar upload do código. 
    

## Uso

1.  Execute o arquivo `main.py`:
    
    ```python main.py```
    
2.  Use a interface para carregar um arquivo ou escrever o código.
3.  Submeta o código para ver os resultados.

### Exemplo de código

```
00000000011000010000000010000011
00000000000100010000000100110011
00000000000100010000000100110011
01000000000100010000000110110011
```

O código de exemplo é uma sequência de ADDI, ADD, ADD e SUB. A memória final esperada é `{'0x2': 12, '0x1': 6, '0x3': 6}`
