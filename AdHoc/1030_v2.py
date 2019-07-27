def josefus(n, k):
	if (n == 1):
		return 1
	else:
		return (josefus(n-1, k) + (k-1)) % n + 1

if __name__ == "__main__":
	cn = int(input())
	for i in range(cn):
		entrada = input().split(" ")
		n = int(entrada[0])
		k = int(entrada[1])
		print("Case %d: %d" %(i+1, josefus(n, k)))