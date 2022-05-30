numero_rainhas = int(input("Digite o número de rainhas: "))
atual_solucao = [0 for rainha in range(numero_rainhas)]
solucoes = []

def verifica_posicao(verifica_linha, verifica_coluna):
    if verifica_linha == 0:
        return True
    
    for linha in range(0, verifica_linha):
        if verifica_coluna == atual_solucao[linha]:
            return False
    
        if abs(verifica_linha - linha) == abs(verifica_coluna - atual_solucao[linha]):
            return False
    
    return True

def posiciona_rainha(linha):
    for coluna in range(numero_rainhas):
        if not verifica_posicao(linha, coluna):
            continue
        
        else:
            atual_solucao[linha] = coluna
            if linha == (numero_rainhas -1):
                solucoes.append(atual_solucao.copy())
            
            else:
                posiciona_rainha(linha + 1)

posiciona_rainha(0)

print(len(solucoes), "solucoes encontradas")
for sol in solucoes:
    for p in sol:
        for c in range(numero_rainhas):
            if c == p:
                print(' R ',end=' ')
            else:
                print(' * ', end=' ')
            
        print()
        
    print()