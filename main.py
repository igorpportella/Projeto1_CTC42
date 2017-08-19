import random

def alfabeto():
    alfabeto = '\n\t'
    for caractere in range(0x0020,0x007F):
        alfabeto += (chr(caractere))
    for caractere in range(0x00A1, 0x0100):
        alfabeto += (chr(caractere))
    return alfabeto

def to_int(letra, alfabeto):
    return alfabeto.find(letra)

def to_char(posicao, alfabeto):
    return alfabeto[posicao]

if (__name__ == '__main__'):
    alfabeto = alfabeto()
    tamanho_alfabeto = len(alfabeto)
    alfabeto_int = [i for i in range(tamanho_alfabeto)]

    entrada = 'machado.txt'
    with open(entrada,'r') as f:
        texto = f.read()
    tamanho_texto = len(texto)
    tabela = [[] for i in range(tamanho_texto)]

    chave = "teste1"
    random.seed(chave)
    chaves = random.sample(range(10000000),tamanho_texto)
    for i in range(tamanho_texto):
        tabela[i] = alfabeto_int[:]
        random.seed(chaves[i])
        random.shuffle(tabela[i])

    texto_cifrado = ""
    for i in range(tamanho_texto):
        texto_cifrado += to_char(tabela[i][to_int(texto[i],alfabeto)],alfabeto)

    saida = 'texto_cifrado.txt'
    with open(saida,'w') as f:
        f.write(texto_cifrado)

    texto_claro = ""
    for i in range(tamanho_texto):
        texto_claro += to_char(tabela[i].index(to_int(texto_cifrado[i],alfabeto)),alfabeto)

    saida2 = 'texto_claro.txt'
    with open(saida2,'w') as f:
        f.write(texto_claro)
