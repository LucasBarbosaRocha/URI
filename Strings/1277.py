casos = int(input())
while casos > 0:
	qtdAlunos = int(input())
	alunos    = input().split(" ")
	presencas = input().split(" ")
	resposta  = ""
	for i in range(qtdAlunos):
		aluno        = alunos[i]
		presenca     = presencas[i]
		qtdPresencas = len(presenca)
		qtdOficial   = 0
		presencaO    = 0 

		for j in range(qtdPresencas):

			if (presenca[j] == 'P'):
				presencaO = presencaO + 1
			if (presenca[j] != 'M'):
				qtdOficial = qtdOficial + 1

		if (qtdOficial > 0):
			frequencia = (presencaO * 100) / qtdOficial

		if (frequencia < 75):
			resposta = resposta + aluno
			resposta = resposta + " "
	print (resposta.strip())




	casos = casos - 1  