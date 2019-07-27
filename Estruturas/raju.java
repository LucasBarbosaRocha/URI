import java.util.Scanner;
import java.util.Arrays;

public class raju
{
  public static void main(String args[])
  {
    Scanner scan = new Scanner(System.in);
    int n, q, vet[], chute, cont = 1;

    n = scan.nextInt();
    q = scan.nextInt();
    while(n != 0 && q != 0)
    {
      vet = new int[n];
      for (int i = 0; i < n; i++) {
        vet[i] = scan.nextInt();
      }

      System.out.println("CASE# " + cont +":");
      Arrays.sort(vet);
      /*ordena(n, vet);*/

      for (int j = 0;j < q; j++) {
        chute = scan.nextInt();

        /*Busca*/
        int k = busca(chute, n, vet) ;
        if(k != -1)
          System.out.println(chute + " found at " + (k+1));
        else
          System.out.println(chute + " not found");
      }


      cont++;
      n = scan.nextInt();
      q = scan.nextInt();
    }

  }

public static void ordena(int n, int v[])
{
  int menor, indice, aux;
  for (int i = 0; i < n; i++) {
    menor = v[i];
    indice = i;
    for (int j = i+1; j < n; j++) {
      if(v[j] < menor){
          menor = v[j];
          indice = j;
        }
    }
    aux = v[i];
    v[i] = menor;
    v[indice] = aux;
  }

}

public static int busca(int x, int n, int v[])
{
  for (int i = 0; i < n; i++) {
    if(x == v[i])
      return i;
  }
  return -1;
}

  public static int buscaBinaria (int x, int n, int v[])
  {
   int e, m, d;
   e = 0; d = n-1;
   while (e <= d) {
      m = (e + d)/2;
      if (v[m] == x)
        return m;
      if (v[m] < x)
        e = m + 1;
      else
        d = m - 1;
   }
   return -1;
}
}