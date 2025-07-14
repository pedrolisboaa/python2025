"""
🚀 Desafio: Sistema de Caixa de Lanchonete
Objetivo: Criar um sistema simples de atendimento de uma lanchonete no terminal.
O sistema deve permitir que o usuário veja o cardápio, faça pedidos, calcule o total, e finalize a compra com troco.

📋 Requisitos:
Mostrar um menu de opções com os produtos disponíveis e seus preços.
Permitir que o cliente selecione mais de um item.
Calcular o valor total da compra.
No final, pedir o valor pago e mostrar o troco.
Usar funções para organizar o código (ex: mostrar_cardapio, fazer_pedido, etc).
"""

CARDAPIO = {
    'X-BURGUER': 10,
    'X-SALADA': 12,
    'BATATA FRITA': 8,
    'REFRIGERANTE': 5,
    'SUCO': 7
}

CARDAPIO_LISTA = list(CARDAPIO)
CARDAPIO_PRECO = list(CARDAPIO.values())

PRECO_FINAL = []
PEDIDO = []


def mostrar_cardapio():
    for i, (chave, valor) in enumerate(CARDAPIO.items(), start=1):
        print(f'{i} - {chave} RS {valor:.2f}')

def adicionar(pedido):
    pedido = pedido
    print(f'Você adicionou um {CARDAPIO_LISTA[pedido - 1]}')
    PEDIDO.append(CARDAPIO_LISTA[pedido - 1])
    PRECO_FINAL.append(CARDAPIO_PRECO[pedido - 1])


while True:
    continuar = input('Deseja fazer escolher um item ou sair: [I] ou [S]: ')
    if continuar.upper() == 'S':
        break
    
    elif continuar.upper() == 'I':
        mostrar_cardapio()
        pedido = int(input('Escolha o numero do item: '))
        

        if pedido in range(1, 6):
            adicionar(pedido)
            
            mais_um = input('Deseja adicionar mais um item: [S] ou [N] ')
            if mais_um.upper() == 'N':
                print(f'Seu pedido foi {PEDIDO} e ficou no valor de R$ {sum(PRECO_FINAL)}')
                print('Pedido finalizado!')
                break

        else:
            print('Não existe no cardápio o item.')
        
    else:
        print('Digite "I" para escolher um item ou "S" para sair.')

print('Muito obrigado! Volte sempre!')
