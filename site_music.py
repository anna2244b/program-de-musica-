# www.thetoneboutique.com.br parecer com isso
v = {'nome': 'v', 'cor': 'rosa', 'categoria': 'iniciantes', 'preço': 1000}
mustang = {'nome': 'mustang', 'cor': 'preto', 'categoria': 'iniciantes', 'preço': 700}
SG = {'nome': 'SG', 'cor': 'verde musgo', 'preço': 1300}
J_master = {'nome': 'J-master', 'cor': 'vermelha', 'preço': 2000}
guitarras = []
guitarras.append(v)
guitarras.append(mustang)
guitarras.append(J_master)
guitarras.append(SG)
# ......................................................................................................
carrinho = []


def guitarra_selecion(guitarras):
    escolha = input('qual nome da guitarra que vc escolheu? ')
    for guitarra in guitarras:
        if escolha.upper() == guitarra.get("nome").upper():
            print(f'ok, vc escolheu {guitarra.get("nome")}  que custa {guitarra.get("preço")}')
            carrinho.append(guitarra)
            print('adicionei isso no seu carrinho')
            return guitarra
    print(f'n achei sua guitarra {escolha}')


while True:
    print('oi, bem vinndo')
    procurar = input('Como vc vai querer procurar pela sua guitarra? Digite 1 para preço, 2 para nome, 3 para cor.  ')
    if procurar == '1':
        for guitarra in guitarras:
            print(f' essa guitarra {guitarra.get("nome")} custa {guitarra.get("preço")} ')
        guitarra_selecion(guitarras)

    if procurar == '2':
        print('temos essas guitarras:')
        for guitarra in guitarras:
            print(f'- {guitarra.get("nome")} ')
        guitarra_selecion(guitarras)

    if procurar == '3':
        for guitarra in guitarras:
            print(f'essa guitarra {guitarra.get("nome")} tem cor {guitarra.get("cor")}')
        guitarra_selecion(guitarras)


    mais_itens = input('vc vai querer mais alguma coisa?')
    if mais_itens == 'sim' or mais_itens == 's':
        print('ok')
    else:
        valor_total = 0
        for guitarra in carrinho:
          valor_total =  guitarra.get("preço") + valor_total
          print(f'o seu pedido eh {guitarra.get("nome")} a cor {guitarra.get("cor")} preço {guitarra.get("preço")}   ')

        print(f'esse é o valor da(s) sua(s) guitarra(s) {valor_total} ')
        forma_pg = input('como vc qr pagar? tem pix, credito e debito')
        if forma_pg == 'pix' or forma_pg == 'credito' or forma_pg == 'debito':
            print('compra concluida! so vou precisar do seu endereço...')
            endereço = input('onde vc mora msm? ')
            print(f'ok enviaremos para {endereço}')
        break
