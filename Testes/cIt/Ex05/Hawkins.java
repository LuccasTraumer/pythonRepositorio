public class Hawkins {
public static void main(String[] args)
    {
        int[] valores = new int[100];
        String valor = "";
        short qtd =0;
        int atual = 0;
        for(short i=1;i <= 8; i++)
        {
            if(i == 1 || i == 4 || i == 6 || i == 8) // Verifica a Centena
            {
                for(short x = 1; x <= 8; x++)
                {
                    if(x == 1 || x == 4 || x == 6 || x == 8 && i != x) // verifica a Dezena
                    {
                        for(short z = 1; z <= 8; z++)
                        {
                            if(z == 1 || z == 4 || z == 6 || z == 8 )// Verifica a Unidade
                            {
                                if( i != x && i != z && x != z) // Verifica se eles são diferentes
                                {
                                    valor = i + "" + x + "" + z + "";
                                    try{
                                        atual = Integer.parseInt(valor);
                                        valores[qtd] = atual;
                                        qtd++;
                                    }catch(NumberFormatException err){}

                                    //System.out.println(valor);
                                }
                            }
                        }
                    }
                }
            }// if
        }// Primeiro for
        int Result = 0;
        for(short i=0; i < qtd;i++)
            Result += valores[i];
        System.out.println(Result);
    }
}