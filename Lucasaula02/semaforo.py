cor =str(input('Digite uma cor entre vermelho, amarelo e verde:')).lower().strip()
# .lower() serve para transformar tudo que o usuario digitar para minusculo
# .strip() serve para tirar espaços antes e depois do texto
# .upper() serve para transformar tudo o que o usuario digitou em maiusculo
if cor == "vermelho":
    print('Pare')
elif cor =="verde":
    print('Acelere')
elif cor =="amarelo":
    print('Atenção')

else:
    print("cor invalida")

