import java.util.Scanner;


public class dois{

	static char[] c = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		String palavra;

		palavra = s.next();

		int k = conta(palavra, palavra.length()-1);

		System.out.println(verifica(palavra));
	}

	public static boolean verifica(String palavra)
	{
		int vogais = conta(palavra, palavra.length()-1);
		int consoantes = palavra.length() - vogais;
		if(vogais >= consoantes)
			return true;
		else
			return false;
	}

	public static int conta(String palavra, int n)
	{
		if(n == 0)
		{
			if(verifichar(palavra.charAt(0)) == true)
				return 1;
			else
				return 0;
		}

		if(verifichar(palavra.charAt(n)) == true)
			return 1 + conta(palavra, n-1);
		else
			return 0 + conta(palavra, n-1);
	}

	public static boolean verifichar(char l)
	{
		for (int i = 0; i < c.length; i++) {
			if (c[i] == l) {
				return true;
			}
		}
		return false;
	}

}