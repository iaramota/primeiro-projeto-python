print("**************************************")
print("------------CALCULADORA--------------")
print("**************************************")

print("escolha uma operação: ")
print(" + para soma")
print(" - para subtração")
print(" * para multiplicação")
print(" / para divisão")

operacao = input("\nQual operação você deseja realizar? ")


if operacao == "+" :
     number_1 = int(input('informe um numero: '))
     number_2 = int(input('mais um numero: '))
     soma = number_1 + number_2
     print(number_1,'+', number_2,'=',soma)

if operacao == "-":
     number_1 = int(input('informe um numero: '))
     number_2 = int(input('mais um numero: '))
     subtração = number_1 - number_2
     print(number_1,'-', number_2,'=',subtracao)

if operacao == "*":
     number_1 = int(input('informe um numero: '))
     number_2 = int(input('mais um numero: '))
     multiplicacao =  number_1 * number_2
     print(number_1,'*', number_2,'=',multiplicacao)

if operacao == "/":
     number_1 = int(input('informe um numero: '))
     number_2 = int(input('mais um numero: '))
     divisao= number_1 / number_2
     print(number_1,'/', number_2,'=',divisao)
else:
     print ("fim! valeu :)")
