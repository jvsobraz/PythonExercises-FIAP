n = int(input("Digite n: "))

div = 1
contador = 0

while div <= n:
    if n % div == 0:
        contador = contador + 1
    div = div + 1

if contador == 2:
    print(n, " eh primo")
else:
    print(n, " nao eh primo")