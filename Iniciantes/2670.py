def min(A, B):
	if A <= B:
		return A
	else:
		return B

A = input()
B = input()
C = input()
auxA = 0
auxB = 0
auxC = 0

auxA = (B*2)+(C*4)
auxB = (A*2)+(C*2)
auxC = (A*4)+(B*2)


print min(auxC, min(auxA, auxB))



