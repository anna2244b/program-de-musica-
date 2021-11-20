#www.thetoneboutique.com.br parecer com isso
v = {'nome': 'V', 'cor': 'rosa', 'categoria': 'iniciantes', 'preço': 1000}
mustang = {'nome': 'mustang', 'cor': 'preto', 'categoria': 'iniciantes', 'preço': 700}
SG = {'nome': 'SG', 'cor': 'verde musgo', 'preço': 1300}
J_master = {'nome': 'J-master', 'cor': 'vermelha', 'preço': 2000}
guitarras = []
guitarras.append(v)
guitarras.append(mustang)
guitarras.append(J_master)
guitarras.append(SG)
print('oi, bem vinndo')
procurar = input('como vc vai querer procurar pela sua guitarra? pelo preço, cor, ou nome?  ')
if procurar == 'preço':
  for guitarra in guitarras:
    print(f' essa guitarra {guitarra.get("nome")} custa {guitarra.get("preço")} ')
if procurar == 'nome':
  print('temos essas guitarras:')
  for guitarra in guitarras:
    print(f'- {guitarra.get("nome")}')
if procurar == 'cor':
  for guitarra in guitarras:
    print(f'essa guitarra {guitarra.get("nome")} tem cor {guitarra.get("cor")}')
