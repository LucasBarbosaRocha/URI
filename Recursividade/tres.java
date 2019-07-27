import java.util.Scanner;

public class tres
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		String r;
		r = s.nextLine();
		System.out.println("entrada " + r);
		r = removeChar(r);
		System.out.println(r);

	}

	public static String removeChar(String c)
	{
		StringBuffer a = new StringBuffer(c);
		String r;
		int tam = a.length();
		for (int i = 0; i < tam; i++) 
		{
			if(a.charAt(i) == ' ')
			{
				for (int j = i; j < tam-1; j++) 
				{
					a.setCharAt(j, a.charAt(j+1));
					a.setCharAt(j+1,' ');
				}
				tam -= 1;
			}
			
		}
		return a.toString();
	}

	public static String removeCharR(String c)
	{


		
	}
}
