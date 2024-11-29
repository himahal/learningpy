'''nota1 = int(input("Qual a sua primeira nota? "))
nota2 = int(input("Qual a sua segunda nota?\n"))

media = (nota1 + nota2)/2

if (media >= 7 and media <= 10):
    print("Parabéns você foi aprovado! Sua média foi", media)
elif (media <7 and media >= 4):
    print("Você pegou final!")
    n3 = int(input("Digite sua nota da final: "))
    media1 = (media + n3)/2
    if (media1 <= 10 and media1 >= 4):
        print("Parabéns!!! Você foi aprovado por média! Sua média final foi:", media1)
    else:
        print("Você foi reprovado!")

else:
    print("Você foi reprovado!")

print("A media foi {}".format(media))
'''
lista = ["carro", "moto", "jetsky", "avião","foguete"]
for i in lista:
    print(i)

