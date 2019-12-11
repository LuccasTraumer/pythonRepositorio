public class Fors
{
	public static void main(String[] args)
	{
		// Não inicio os For's em 0(Zero) pois caso multiplique sempre vai dar Zero, então posso comecar em 1.
		int Result = 0;
		        int result =0;
		        for(int i=1;i < 9;i++) // Unidade de Milhar
		        {
		            for(int x=1;x < 9;x++) //Centena
		            {
		                for(int z = 1; z < 9;z++)//Dezena
		                {
		                    for(int k =1; k < 9;k++) // Unidade
		                    {
		                        result = i*x*z*k; // Faz as operações
		                        if (result == 100) // Verifica se o Resultado das Mult são iguais a 100, caso seja Result
		                        					// é um Contador que no final ira moestra quantos valores multiplicando seu algarismo dão 100.
		                            Result++;
		                    }
		                }
		            }
		        }
		// só que com 3 Numeros poder fazer mais 3
		Result+=3;
        System.out.println("Numero entre 0 e 9999 que dão 100: "+ Result);

	}//end main
}// end class