import math
import copy

x = "X"
o = "O"

def estado_inicial():
    inicio_jogo = [ [None, None, None],
                    [None, None, None],
                    [None, None, None]]
    return inicio_jogo

def eh_estado_final(tabuleiro_atual):
    no_marcados = 0

    for i in range(3):
        for j in range(3):
            if tabuleiro_atual[i][j]:
                no_marcados = no_marcados + 1
    
    if no_marcados == 9:
        return True

    # LINHAS
    for i in range(3):
        if tabuleiro_atual[i][0] == tabuleiro_atual[i][1] and tabuleiro_atual[i][0] == tabuleiro_atual[i][2]:
            if tabuleiro_atual[i][0] is None:
                return False
            else: return True

    # COLUNAS
    for i in range(3):
        if tabuleiro_atual[0][i] == tabuleiro_atual[1][i] and tabuleiro_atual[0][i] == tabuleiro_atual[2][i]:
            if tabuleiro_atual[0][i] is None:
                return False
            else: return True
    
    
    # DIAGONAL            
    if tabuleiro_atual[0][0] == tabuleiro_atual[1][1] and tabuleiro_atual[0][0] == tabuleiro_atual[2][2]:
        if tabuleiro_atual[0][0] is None:
            return False
        else: return True
    elif tabuleiro_atual[0][2] == tabuleiro_atual[1][1] and tabuleiro_atual[0][2] == tabuleiro_atual[2][0]:
        if tabuleiro_atual[0][2] is None:
            return False
        else: return True

    return False

def printar_tabuleiro(tabuleiro):
    tabuleiro_atual = copy.deepcopy(tabuleiro)
    contador = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro_atual[i][j] is None:
                tabuleiro_atual[i][j] = contador
            contador += 1

    tabuleiro = '''
                 |         |         
            {}    |    {}    |    {}    
        _________|_________|_________
                 |         |         
            {}    |    {}    |    {}    
        _________|_________|_________
                 |         |         
            {}    |    {}    |    {}    
                 |         |         
                '''.format(tabuleiro_atual[0][0], tabuleiro_atual[0][1], tabuleiro_atual[0][2], 
                tabuleiro_atual[1][0], tabuleiro_atual[1][1], tabuleiro_atual[1][2], 
                tabuleiro_atual[2][0], tabuleiro_atual[2][1], tabuleiro_atual[2][2])
    print(tabuleiro)

def vencedor(tabuleiro):

    # COLUNAS
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]:
            return tabuleiro[0][i]
    
    
    # DIAGONAL            
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]:
        return tabuleiro[0][2]

    # LINHAS
    for coluna in tabuleiro: 
        if coluna[0] == coluna[1] and coluna[0] == coluna[2]:
            return coluna[0]

    return None

def jogadas_possiveis(tabuleiro):
    jogadas = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] is None: 
                jogadas.append([i,j])
    return jogadas

def proximo_jogador(tabuleiro):
    contador = {x: 0,
                o: 0,
                None: 0}
    for i in range(3):
        for j in range(3):
            contador[tabuleiro[i][j]] += 1

    if contador[x] > contador[o]:
        return o
    else: return x
                
def utilidade(estado_atual):
    if not vencedor(estado_atual):
        return 0

    elif vencedor(estado_atual) == x:
        return 1

    elif vencedor(estado_atual) == o:
        return -1

def valor_max(estado_atual):
    if eh_estado_final(estado_atual):
        return utilidade(estado_atual)

    v = -math.inf

    for jogada in jogadas_possiveis(estado_atual):
        tabuleiro_aux = copy.deepcopy(estado_atual)
        tabuleiro_aux[jogada[0]][jogada[1]] = proximo_jogador(tabuleiro_aux)
        v = max(v, valor_max(tabuleiro_aux))

    return v 

def valor_min(estado_atual):
    if eh_estado_final(estado_atual):
        return utilidade(estado_atual)
    
    v = math.inf
    for jogada in jogadas_possiveis(estado_atual):
        tabuleiro_aux = copy.deepcopy(estado_atual)
        tabuleiro_aux[jogada[0]][jogada[1]] = proximo_jogador(tabuleiro_aux)
        v = min(v, valor_max(tabuleiro_aux))
    return v    

def minimax(tabuleiro):
    jogador_atual = proximo_jogador(tabuleiro)

    if jogador_atual == x:
        v = -math.inf

        for jogada in jogadas_possiveis(tabuleiro):
            tabuleiro_aux = copy.deepcopy(tabuleiro)
            tabuleiro_aux[jogada[0]][jogada[1]] = proximo_jogador(tabuleiro_aux)

            v_aux = valor_min(tabuleiro_aux)

            if v_aux > v:
                v = v_aux
                melhor_jogada = jogada
    else:
        v = math.inf

        for jogada in jogadas_possiveis(tabuleiro):
            tabuleiro_aux = copy.deepcopy(tabuleiro)
            tabuleiro_aux[jogada[0]][jogada[1]] = proximo_jogador(tabuleiro_aux)

            v_aux = valor_max(tabuleiro_aux)

            if v_aux < v:
                v = v_aux
                melhor_jogada = jogada

    return melhor_jogada

def entrada_de_jogada(tabuleiro):
    jogada_humano = int(input("Digite sua jogada:"))
    if jogada_humano == 0:
        tabuleiro[0][0] = o
        return tabuleiro

    elif jogada_humano == 1:
        tabuleiro[0][1] = o
        return tabuleiro

    elif jogada_humano == 2:
        tabuleiro[0][2] = o
        return tabuleiro

    elif jogada_humano == 3:
        tabuleiro[1][0] = o
        return tabuleiro

    elif jogada_humano == 4:
        tabuleiro[1][1] = o
        return tabuleiro

    elif jogada_humano == 5:
        tabuleiro[1][2] = o
        return tabuleiro

    elif jogada_humano == 6:
        tabuleiro[2][0] = o
        return tabuleiro

    elif jogada_humano == 7:
        tabuleiro[2][1] = o
        return tabuleiro

    elif jogada_humano == 8:
        tabuleiro[2][2] = o
        return tabuleiro

    else:
        print("Entrada invalida")
        return entrada_de_jogada(tabuleiro)

def main():
        
    jogo = estado_inicial()
    jogada_pc = minimax(jogo)
    jogo[jogada_pc[0]][jogada_pc[1]] = x
    printar_tabuleiro(jogo)

    while not eh_estado_final(jogo):
        jogo = entrada_de_jogada(jogo)

        jogada_pc = minimax(jogo)
        jogo[jogada_pc[0]][jogada_pc[1]] = x
        printar_tabuleiro(jogo)
        
    printar_tabuleiro(jogo)
    if vencedor(jogo) is None:
        print("EMPATE")
    else:
        print("{} FOI O VENCEDOR".format(vencedor(jogo)))


if __name__ == "__main__":
    main()