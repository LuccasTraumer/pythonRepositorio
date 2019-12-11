public class Blocos
{
	public static void main(String[] args)
	{
		String[] armazenados = new String[100]; // Cria um Vetor para armazenar os Valores
        String valorAtual = ""; // Variavel que vai receber o valor do for
        int qtd = 0; // Contador do vetor
        for(int numero=1; numero < 1958;numero++) // um for de 1 a 1958 que foi pedido
        {
            if(numero > 100 && numero < 1958) // Condição para os Blocos de 1's
            {
                valorAtual = numero+"";
                char centena = ' ';
                char dezena = ' ';
                char unidade = ' ';
                char milhar = ' ';
                if(numero < 1000) // Se o valor for menor que 1000, tem apenas 3 algarismos
                {
                    centena = valorAtual.charAt(0);
                    dezena = valorAtual.charAt(1); // pega o segundo algarismo
                    unidade = valorAtual.charAt(2); // pega o terceiro algarismo
                    if (unidade == dezena && dezena == centena)  // Se todos algarismos forem iguais
                    {
                        armazenados[qtd] = valorAtual; // armazena no vetor
                        qtd++;
                    }
                }
                else // se o valor for maior que 1000
                {
                    centena = valorAtual.charAt(0);
                    dezena = valorAtual.charAt(1);
                    unidade = valorAtual.charAt(2);
                    milhar = valorAtual.charAt(3);
                    if (unidade == dezena && dezena == centena && milhar == centena) {
                        armazenados[qtd] = valorAtual;
                        qtd++;
                    }
                }

            }
        }
        int valor = Integer.parseInt(armazenados[qtd-1]); // Converto o valor para saber o prox
        int prox = valor+1; // pego o valor do prox valor
        int Result =0; // contador de quantos caracters vai ter s
        String val = valor + ""+ prox+""; // coloco em uma String os dois valores juntos
        for(int i = 0; i < val.length();i++)
            if(val.charAt(i) == '1') // se o valor for igual a 1
                Result++; // Conta
        System.out.println(Result);


	}// end main
}// end class