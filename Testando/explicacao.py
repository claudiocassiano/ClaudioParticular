print("Programa iniciado!\nCriando variáve ativo e atribuindo o valor booleano True:\n")
ativo = True
print("cCondição While será iniciada agora!\nWhile significa enquanto, portanto while ativo signfica enquanto verdadeiro faça: \n")
while ativo:
    print("agora entrado no Try que signfica tentar ou tente fazer o código abaixo: ")
    
    # procurar sobre try except finally!
    try:
        print("mostrando a primeira string que pede para informar os dados do raio e da altura logo abaixo:\n")
        print("Informe agora os dados para obtenção do volume do cilindro: ")
        print("duas variáveis serão criadas agora para receber as informações do usuário:\n")
        
        # o float nesse caso está forçando a entrada a ser desse tipo. Algumas vezes é inressante usar str() para poder tratar a informação que entra do usuário e evitar erro
        raioCilindro = float(input("raio(r) -> "))
        alturaCilindro = float(input("altura(h) -> "))
        print("Na linha abaixo temos o calculo do volume\nCalculando volume agora:\n")
        
        # parênteses forçam precedência
        volume = (3.14 * (raioCilindro ** 2)) * alturaCilindro
        print("Agora será informado o resultado:\n")
        
        # esse f antes das aspas é o Format! É a forma mais simples do format pra organizar varipaveis dentro dos textos
        print(f"Volume do Cilindro: 3.14 * r² * h = {volume}³")
        
        
        print("uma nova variável será criada pra saber se quer sair ou continuar\n")
        onOff = str(input("S para sair - C para continuar: "))
        print("Recebida a informação do usuário ocorrerá os testes if pra saber o que você escolheu\n")
        
        if onOff == "S" or onOff == "s": 
            print("Saindo do programa!")
            ativo = False
            # você pode usar o break aq no lugar de mudar pra False
        elif onOff in "Cc": # segunda forma de fazer a mesma comparação acima do S
            print("Reiniciando!")
            ativo = True
        else:
            # colocar esse raise chama a parte do Except ValueError abaixo. Entre aspas do print cabe qualquer informação, tanto aqui como lá
            raise ValueError("Informação não reconhecida! Reiniciando aplicação!") 
    except ValueError as e:
        print("Erro", e)
