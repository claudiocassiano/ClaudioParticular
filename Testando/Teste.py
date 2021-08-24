
print("Coloque sua senha para ter acesso ao sistema\n")

senha = str(input("Digite sua senha, - admin ou user: \n"))

if(senha == "admin"):
    print("Olá, Administrador.")
elif(senha == "user"):
    print("Olá, Usuário.")
else:
    print("Acesso negado, Verifique sua senha.")

