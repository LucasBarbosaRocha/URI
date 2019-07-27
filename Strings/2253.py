# A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
# A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
# Além disso, a senha pode ter de 6 a 32 caracteres.

while True:
	try:
		error = 0
		entrada = input()
		tam = len(entrada)
		if (tam < 6 or tam > 32):
			print("Senha invalida.")
		else:
			minu = maiu = numero = 0
			for i in range(tam):
				num = ord(entrada[i])
				if (num >= 48 and num <= 57):
					numero = numero + 1 
				elif (num >= 97 and num <= 122):
					minu = minu + 1
				elif (num >= 65 and num <= 90): 
					maiu = maiu + 1
				else:
					numero = minu = maiu = -1
					break
			if (numero >= 1 and minu >= 1 and maiu >= 1):
				print("Senha valida.")
			else:
				print("Senha invalida.")
	except:
		break
