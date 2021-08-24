print("Programa iniciado!\nCriando variáve ativo e atribuindo o valor booleano True:\n")
ativo = True
print("cCondição While será iniciada agora!\nWhile significa enquanto, portanto while ativo signfica enquanto verdadeiro faça: \n")
while ativo:
    print("agora entrado no Try que signfica tentar ou tente fazer o código abaixo: ")
    try:
        print("mostrando a primeira string que pede para informar os dados do raio e da altura logo abaixo:\n")
        print("Informe agora os dados para obtenção do volume do cilindro: ")
        print("duas variáveis serão criadas agora para receber as informações do usuário:\n")
        raioCilindro = float(input("raio(r) -> "))
        alturaCilindro = float(input("altura(h) -> "))
        print("Na linha abaixo temos o calculo do volume\nCalculando volume agora:\n")
        volume = (3.14 * (raioCilindro ** 2)) * alturaCilindro
        print("Agora será informado o resultado:\n")
        print(f"Volume do Cilindro: 3.14 * r² * h = {volume}³")
        print("uma nova variável será criada pra saber se quer sair ou continuar\n")
        onOff = str(input("S para sair - C para continuar: "))
        print("Recebida a informação do usuário ocorrerá os testes if pra saber o que você escolheu\n")
        if onOff == "S" or onOff == "s":
            print("Saindo do programa!")
            ativo = False
            # você pode usar o break aq no lugar de mudar pra False
        elif onOff == "C" or onOff == "c":
            print("Reiniciando!")
            ativo = True
        else:
            raise ValueError("Informação não reconhecida! Reiniciando aplicação!")
    except ValueError as e:
        print("Erro", e)