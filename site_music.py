
#www.thetoneboutique.com.br parecer com isso
v = {'nome': 'v', 'cor': 'rosa', 'categoria': 'iniciantes', 'preço': 1000}
mustang = {'nome': 'mustang', 'cor': 'preto', 'categoria': 'iniciantes', 'preço': 700}
SG = {'nome': 'SG', 'cor': 'verde musgo', 'preço': 1300}
J_master = {'nome': 'J-master', 'cor': 'vermelha', 'preço': 2000}
guitarras = []
guitarras.append(v)
guitarras.append(mustang)
guitarras.append(J_master)
guitarras.append(SG)
#........................................................................................................


def guitarra_selecion(guitarras):
  escolha = input('qual nome da guitarra que vc escolheu? ')
  for guitarra in guitarras:
    if escolha.upper() == guitarra.get("nome").upper():
      print(f'ok, vc escolheu {guitarra.get("nome")}  que custa {guitarra.get("preço")}')
      return guitarra
  print(f'n achei sua guitarra {escolha}')



print('oi, bem vinndo')
procurar = input('como vc vai querer procurar pela sua guitarra? digite 1 para  preço, 2 para nome, 3 para cor?  ')
if procurar == '1':
  for guitarra in guitarras:
    print(f' essa guitarra {guitarra.get("nome")} custa {guitarra.get("preço")} ')
  guitarra_selecion(guitarras)

if procurar == '2':
  print('temos essas guitarras:')
  for guitarra in guitarras:
    print(f'- {guitarra.get("nome")}')
  guitarra_selecion(guitarras)

if procurar == '3':
  for guitarra in guitarras:
    print(f'essa guitarra {guitarra.get("nome")} tem cor {guitarra.get("cor")}')
  guitarra_selecion(guitarras)
