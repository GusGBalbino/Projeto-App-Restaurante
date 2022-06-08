def criar_pedido (menu, pedidos_feitos):
    pedidos_feitos.append(menu)




def cancelar_pedido(pedidos_feitos, pedidos_cancelados):
    if not pedidos_feitos:
        print('Nenhum pedido para cancelar.')
        return
    last_pedido = pedidos_feitos.pop()
    pedidos_cancelados.append(last_pedido)




def recuperar_pedido(pedidos_feitos, pedidos_cancelados):
    if not pedidos_cancelados:
        print('Nenhum pedido para recuperar.')
        return
    last_cancelado = pedidos_cancelados.pop()
    pedidos_feitos.append(last_cancelado)




def listar_pedidos(pedidos_feitos):
    if not pedidos_feitos:
        print('Não existem pedidos feitos')
    else:
        print('Pedidos feitos: ')
        print(pedidos_feitos)




if __name__ == '__main__':
    pedidos_feitos = []
    pedidos_cancelados = []


    while True:
        menu = input('DIGITE O PEDIDO ou C - Cancelar último pedido | R - Recuperar ultimo pedido cancelado | L - Listar os pedidos já feitos \n')
        if menu == 'C':
            cancelar_pedido(pedidos_feitos, pedidos_cancelados)
            continue
        elif menu == 'R':
            recuperar_pedido(pedidos_feitos, pedidos_cancelados)
            continue
        elif menu == 'L':
            listar_pedidos(pedidos_feitos)
            continue

        criar_pedido(menu, pedidos_feitos)
