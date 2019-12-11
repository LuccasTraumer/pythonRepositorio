public class Analise
{
	public static void main(String[] args)
	{
		// Numero 1,4,6,8, numeros de 3 algarismos distintos
		// posso fazer um for e ir incluindo em um vetor de inteiro depois somar

		int[] valores = new int[100];
		String valor = "";
		int qtd =0;
		int atual = 0;
		for(int i=1;i < 8; i++)
		{
			if(i == 1 || i == 4 || i == 6 || i == 8) // Verifica a Centena
			{
				for(int x = 1; x < 8; x++)
				{
					if(x == 1 || x == 4 || x == 6 || x == 8) // verifica a Dezena
					{
						for(int z = 1; z < 8; z++)
						{
							if(z == 1 || z == 4 || z == 6 || z == 8)// Verifica a Unidade
							{
								valor = i+x+z+"";
								System.out.println(valor);
							}
						}
					}
				}
			}// if




		}// Primeiro for
	}// metodo main
}// end classe