cor =str(input('Digite uma cor entre vermelho, amarelo e verde:')).lower().strip()

match cor:
    case "vermelho":
        print("pare")
    case "verde":
        print("acelere")
    case "amarelo":
        print("atenção")
    case _:
        print('cor indisponivel')
