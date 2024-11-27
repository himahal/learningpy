nota1 = int(input("Qual a sua primeira nota? "))
nota2 = int(input("Qual a sua segunda nota?\n"))

media = (nota1 + nota2)/2

if (media >= 7 and media <= 10):
    print("Parabéns você foi aprovado! Sua média foi", media)
elif (media <7 and media >= 4):
    print("Você pegou final!")
else:
    print("Você foi reprovado!")




