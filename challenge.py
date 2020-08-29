#PacklOt-Challenge
#Leonardo de Souza


def multiplicacao(a, b):
		soma = 0
		contador = 0

		while contador<b:
			soma = soma + a
			contador = contador + 1

		return soma

def exponencial(x, n):
	exp = x
	contador = 1 

	while contador<n:
		exp = multiplicacao(exp, x)
		contador = contador + 1

	return exp


