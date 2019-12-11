public class DiferencaImparPar{

	public static void main(String[] args)
	{
		short ano = 1985; // Atributo ano
        int Result = 0; // variavel que vai ser Atribuida o resultado
        if(ano % 2 != 0) // Se o numero não for Par
            Result = ano/2 + 1; // Dividi ele por dois vai tem metade impar e metade Par e Incrementa mais um do ano final que é impra
        else // Se o numero for par
            Result = ano/2; // Dividi ele por 2 e vai ser metade impra e metade par.

        System.out.println(Result);
	}
}