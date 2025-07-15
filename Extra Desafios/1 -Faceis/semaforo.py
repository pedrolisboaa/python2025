
while True:
    cor = input('Digite a cor do semáforo (ou "sair"para encerrar): ')
    if cor.lower() == 'verde':
        print(f'✅ Pode atravessar.')
    elif cor.lower() == 'vermelho':
        print(f'⛔ Espere. Não atravesse!')
    elif cor.lower() == 'amarelo':
        print(f'🟡 Atenção! Prepare-se para parar.')
    elif cor.lower() == 'sair':
        print('Encerrando programa...')
        break
    else:
        print('❌ Cor inválida!')
    