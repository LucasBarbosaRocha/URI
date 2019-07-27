import java.util.Scanner;

public class matrizR{

	public static void main(String args[])
	{

		Scanner s = new Scanner(System.in);

		int m[][], n, soma;

		n = s.nextInt();

		m = new int[n][n];

		for (int i = 0;i < n; i++) {
			for (int j = 0;j < n ; j++) {
				m[i][j] = s.nextInt();
			}
		}

		soma = somaM(m,0,0,n);

		System.out.println("A soma é " + soma);

	}

	public static int somaM(int m[][], int i, int j, int n)
	{
		int s = 0;
		if(i == n)
			return 0;
		if(j < n)
		{
			s += m[i][j];
			return s += somaM(m,i,j+1,n);
		} else 
			return s += somaM(m,i+1,0,n);
	}
}