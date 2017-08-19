def alfabeto():
    alfabeto = []
    for caractere in range(0x20,0x7F):
        alfabeto.append(chr(caractere))
    for caractere in range(0xC0,0xFC):
        alfabeto.append(chr(caractere))


def to_int(letra):
    alfabeto = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÇÈÉÊËÌÍ'
    return alfabeto.find(letra)

def to_char(posicao):
    alfabeto = ' !"#$%&()*+,-./0123456789:;<?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    return alfabeto[posicao]

if (__name__ == '__main__'):
