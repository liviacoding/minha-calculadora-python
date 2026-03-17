import funcao

print("------ CALCULADORA DA LIVIA------")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input('Digite o segundo número: '))

print("\nEscolhaa a operação: + - * /")


operacao = input("\nQual Operação deseja fazer?: ")

if operacao == "+":
    print(f"\nO resultado da operação é: {funcao.soma(n1,n2)}")

elif operacao == "-":
     print(f"\nO resultado da operação é: {funcao.subtracao(n1,n2)}")

elif operacao == "*":
    print(f"\nO resultado da operação é: {funcao.multiplicacao(n1,n2)}")

elif operacao == "/":
    print(f"\nO resultado da operação é: {funcao.divisao(n1,n2)}")
