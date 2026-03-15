print("------ CALCULADORA DA LIVIA------")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input('Digite o segundo número: '))

print("\nEscolhaa a operação:")
print("+ para somar")
print("* para multiplicar")
print("/ para dividir")
print("- para Subtrair")

operacao = input("\nQual Operação deseja fazer?: ")

if operacao == "+":
    resultado = n1 + n2
    print("\nO resultado da operação é: {}".format(resultado))
elif operacao == "-":
    resultado = n1 - n2
    print("\nO resultado da operação é: {}".format(resultado))
elif operacao == "*":
    resultado = n1 * n2
    print("\nO resultado da operação é: {}".format(resultado))
elif operacao == "/":
    resultado = n1 / n2
    print("\nO resultado da operação é: {}".format(resultado))
else:
    print("\nERRO : Não é possivel dividir por ZERO!")
    print("\nOperação inválida!")

